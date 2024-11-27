import os, torch

from transformers import (
    AutoModelForCausalLM,
    AutoTokenizer,
    BitsAndBytesConfig
)

from .utils import download_model
from .config import system_role, add_assistant_answers_to_history

from .config import (
    default_checkpoint,
    default_max_seq,
    default_saving_dir,
    default_save_history,
    default_max_history_size
)


class PozdnyakovChatBot:
    def __init__(
        self,
        checkpoint: str | int = default_checkpoint,
        saving_dir: str = default_saving_dir,
        max_seq: int = default_max_seq,
        save_history: bool = default_save_history,
        max_history_size: int = default_max_history_size,
        model_path: str = None,
    ):
        """Constructor of PozdnyakovChatBot class.

        :param checkpoint: Checkpoint (weights) index.
        :param model_path: Path to an existing model.
        :param saving_dir: Path to save loaded weights.
        :param max_seq: Max length of generated sequence.
        """

        if isinstance(checkpoint, int):
            checkpoint = str(checkpoint)
        if model_path is None:
            download_model(checkpoint=checkpoint, saving_dir=saving_dir)
            model_path = os.path.join(saving_dir, f"checkpoint-{checkpoint}")

        self.max_seq = max_seq
        self.save_history = save_history
        self.max_history_size = max_history_size

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

        self.terminators = [
            self.tokenizer.eos_token_id,
            self.tokenizer.convert_tokens_to_ids("<|eot_id|>"),
        ]

        self.model = AutoModelForCausalLM.from_pretrained(
            model_path,
            device_map="auto",
            quantization_config=self.bnb_config,
            attn_implementation="eager"
        )

    def __update_history(self):
        self.history = [self.history[0]] + self.history[2:]


    def generate(self, prompt: str, messages: dict = None) -> str:
        """Get answer to a prompt.

        :param prompt: Prompt to a model.
        :param messages: History of conversations.
        :return: Model's answer.
        """
        if messages is None:
            if not self.save_history:
                messages = [
                    {"role": "system", "content": system_role},
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
            max_new_tokens=self.max_seq,
            eos_token_id=self.terminators
        )
        model_response = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        processed_response = model_response[model_response.find("assistant\n") + 11:]

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
