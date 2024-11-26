import os
import io
import zipfile
import requests


available_checkpoints = [
    "1000", "2200", "3300", "3695"
]


def download_model(checkpoint: str = "3695", saving_dir: str = "weights"):
    if checkpoint not in available_checkpoints:
        raise FileNotFoundError(
            f"Checkpoint {checkpoint} is not available. Available checkpoints: {available_checkpoints}"
        )

    saving_path = os.path.join(saving_dir, f"checkpoint-{checkpoint}")
    if not os.path.isdir(saving_path):
        downloading_url = f"https://storage.yandexcloud.net/pozdnyakov-ai/checkpoint-{checkpoint}.zip"
        response = requests.get(downloading_url)
        downloaded_archive = zipfile.ZipFile(io.BytesIO(response.content))

        if not os.path.isdir(saving_dir):
            os.mkdir(saving_dir)

        downloaded_archive.extractall(path=saving_dir)
