from transformers import pipeline, AutoProcessor, AutoModelForSpeechSeq2Seq

from torch import float16 as torch_dtype


use_gpu = True
stt_model = "openai/whisper-large-v3"


class SpeechRecognition:
    """Class made for Speech-To-Text task."""
    def __init__(self, use_cuda: bool = use_gpu, model_name: str = stt_model):
        """Constructor of a SpeechRecognition class.

        :param use_cuda: 'True' if you need to use GPU.
        :param model_name: STT model's name.
        """
        self.device = "cuda" if use_cuda else "cpu"

        self.processor = AutoProcessor.from_pretrained(model_name)

        self.model = AutoModelForSpeechSeq2Seq.from_pretrained(
            pretrained_model_name_or_path=model_name,
            torch_dtype=torch_dtype,
            low_cpu_mem_usage=True
        ).to(self.device)

        self.pipe = pipeline(
            task="automatic-speech-recognition",
            model=self.model,
            device=self.device,
            torch_dtype=torch_dtype,
            tokenizer=self.processor.tokenizer,
            feature_extractor=self.processor.feature_extractor,
            chunk_length_s=30,
            batch_size=16
        )

    def __call__(self, audio_file: str, *args, **kwargs) -> str:
        """Get brief from audio file

        :param audio_file: Audio file path.
        :return: Text of audio file.
        """
        return self.pipe(audio_file)["text"]
