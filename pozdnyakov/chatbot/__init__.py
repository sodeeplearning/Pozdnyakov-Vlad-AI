import os, torch

from transformers import (
    AutoModelForCausalLM,
    AutoTokenizer,
    BitsAndBytesConfig,
    GenerationConfig
)

from .utils import download_model
from .config import system_role, add_assistant_answers_to_history

from .config import (
    default_checkpoint,
    default_max_seq,
    default_min_seq,
    default_saving_dir,
    default_save_history,
    default_max_history_size,
    default_temperature,
    default_repetition_penalty,
    default_do_sample,
    default_confidence_threshold,
    default_top_k,
    default_print_dialogues
)


class PozdnyakovChatBot:
    def __init__(
        self,
        checkpoint: str | int = default_checkpoint,
        saving_dir: str = default_saving_dir,
        model_path: str = None,

        max_seq: int = default_max_seq,
        min_seq: int = default_min_seq,
        confidence_threshold: float = default_confidence_threshold,
        save_history: bool = default_save_history,
        max_history_size: int = default_max_history_size,
        temperature: float = default_temperature,
        repetition_penalty: float = default_repetition_penalty,
        top_k: int = default_top_k,
        do_sample: bool = default_do_sample,
        print_dialogues: bool = default_print_dialogues
    ):
        """Constructor of PozdnyakovChatBot class.

        :param checkpoint: Checkpoint (weights) index.
        :param saving_dir: Path to save loaded weights.
        :param model_path: Path to an existing model.
        :param max_seq: Max length of generated sequence.
        :param min_seq: Min length of generated sequence.
        :param confidence_threshold: Min probability of token to generate.
        :param save_history: 'True' if you need to save you conversations.
        :param max_history_size: If history size will exceed this value - history will clean every message
        :param temperature: Value of model's 'creativity'
        :param repetition_penalty: Value of penalty of repeated words.
        :param top_k: Model will choose only top-15 tokens with the bests probability.
        :param do_sample: Make generations as a sample.
        :param print_dialogues: 'True' if you need to see all conversations on screen.
        """

        if isinstance(checkpoint, int):
            checkpoint = str(checkpoint)
        if model_path is None:
            download_model(checkpoint=checkpoint, saving_dir=saving_dir)
            model_path = os.path.join(saving_dir, f"checkpoint-{checkpoint}")

        self.save_history = save_history
        self.max_history_size = max_history_size
        self.print_dialogues = print_dialogues

        self.history = [
            {"role": "system", "content": system_role}
        ]

        self.bnb_config = BitsAndBytesConfig(
            load_in_4bit=True,
            bnb_4bit_quant_type="nf4",
            bnb_4bit_compute_dtype=torch.float16,
            bnb_4bit_use_double_quant=True,
        )

        self.tokenizer = AutoTokenizer.from_pretrained(model_path)

        self.tokenizer.pad_token_id = self.tokenizer.eos_token_id

        self.terminators = [
            self.tokenizer.eos_token_id,
            self.tokenizer.convert_tokens_to_ids("<|eot_id|>")
        ]

        self.generation_config = GenerationConfig(
            temperature=temperature,
            max_new_tokens=max_seq,
            min_new_tokens=min_seq,
            eos_token_id=self.terminators,
            repetition_penalty=repetition_penalty,
            do_sample=do_sample,
            assistant_confidence_threshold=confidence_threshold,
            top_k=top_k
        )

        self.model = AutoModelForCausalLM.from_pretrained(
            model_path,
            device_map="auto",
            quantization_config=self.bnb_config,
            attn_implementation="eager",
        )

    def __update_history(self):
        self.history = [self.history[0]] + self.history[2:]

    @staticmethod
    def __postprocess_output(model_response: str) -> str:
        assistant_response = model_response[model_response.find("assistant\n") + 11:]
        cleaned = assistant_response.replace("assistant", "")

        if "_ComCallableWrapper" in cleaned:
            cleaned = cleaned[:cleaned.find("_ComCallableWrapper")]

        return cleaned

    def generate(self, prompt: str, messages: dict = None) -> str:
        """Get answer to a prompt.

        :param prompt: Prompt to a model.
        :param messages: History of conversations.
        :return: Model's answer.
        """
        if messages is None:
            if not self.save_history:
                messages = [
                    {"role": "user", "content": prompt}
                ]
            else:
                self.history.append({"role": "user", "content": prompt})
                messages = self.history


        input_ids = self.tokenizer.apply_chat_template(
            messages,
            add_generation_prompt=True,
            return_tensors="pt"
        ).to(self.model.device)

        outputs = self.model.generate(
            input_ids,
            generation_config=self.generation_config
        )
        model_response = self.tokenizer.decode(outputs[0], skip_special_tokens=True)

        processed_response = self.__postprocess_output(model_response)

        if self.print_dialogues:
            print(f"User: {prompt}")
            print(f"Assistant: {processed_response}")

        if self.save_history and add_assistant_answers_to_history:
            self.history.append({"role": "assistant", "content": processed_response})
        if len(self.history) > self.max_history_size:
            self.__update_history()

        return processed_response


    def __call__(self, prompt: str, messages: dict = None) -> str:
        """Get answer to a prompt.

        :param prompt: Prompt to a model.
        :param messages: History of conversations.
        :return: Model's answer.
        """
        return self.generate(
            prompt=prompt,
            messages=messages
        )
