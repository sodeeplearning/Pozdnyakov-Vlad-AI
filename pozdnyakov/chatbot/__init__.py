import os, torch

from transformers import (
    AutoModelForCausalLM,
    AutoTokenizer,
    BitsAndBytesConfig
)

from .utils import download_model


class PozdnyakovChatBot:
    def __init__(
        self,
        checkpoint: str | int = "3695",
        model_path: str = None,
        saving_dir: str = "weights",
        max_seq: int = 128
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

        self.bnb_config = BitsAndBytesConfig(
            load_in_4bit=True,
            bnb_4bit_quant_type="nf4",
            bnb_4bit_compute_dtype=torch.float16,
            bnb_4bit_use_double_quant=True,
        )

        self.tokenizer = AutoTokenizer.from_pretrained(model_path)

        self.terminators = [
            self.tokenizer.eos_token_id,
            self.tokenizer.convert_tokens_to_ids("<|eot_id|>")
        ]

        self.model = AutoModelForCausalLM.from_pretrained(
            model_path,
            device_map="auto",
            quantization_config=self.bnb_config,
            attn_implementation="eager"
        )

    def generate(self, prompt: str, messages: dict = None) -> str:
        """Get answer to a prompt.

        :param prompt: Prompt to a model.
        :param messages: History of conversations.
        :return: Model's answer.
        """
        if messages is None:
            messages = [
                {"role": "user", "content": prompt}
            ]

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
        return model_response[model_response.find("assistant\n") + 11:]

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
