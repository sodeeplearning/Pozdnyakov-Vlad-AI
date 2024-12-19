import json
import os

from trainer import Trainer, TrainerArgs

from TTS.config.shared_configs import BaseDatasetConfig
from TTS.tts.datasets import load_tts_samples

from TTS.tts.configs.vits_config import VitsConfig
from TTS.tts.models import setup_model


def formater(root_path, manifest_file, **kwargs):
    with open(os.path.join(root_path, manifest_file), "r") as json_file:
        return json.load(json_file)


model_name = "tts_models/ru/ru_open_tts/vits"
output_path = ""
dataset_config = BaseDatasetConfig(
    formatter="vctk",
    meta_file_train="processed_tts_dataset.json",
    path=r"C:\Users\vital\PycharmProjects\Pozdnyakov-Vlad-AI\dataset\tts_dataset",
    language="ru"
)

config = VitsConfig(
    batch_size=10,
    eval_batch_size=1,
    epochs=100,
    text_cleaner="phoneme_cleaners",
    use_phonemes=True,
    phoneme_language="ru",
    phoneme_cache_path="phoneme_cache",
    print_step=5,
    print_eval=True,
    mixed_precision=False,
    output_path=output_path,
    datasets=[dataset_config],
    phonemizer="gruut",
)
model = setup_model(config=config)

train_samples, eval_samples = load_tts_samples(
    dataset_config,
    formatter=formater
)

trainer = Trainer(
    TrainerArgs(
        best_path="best_training",
    ),
    config,
    output_path,
    model=model,
    train_samples=train_samples,
    eval_samples=eval_samples
)

trainer.fit()
