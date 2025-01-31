import os
from os import remove


from .stt import SpeechRecognition
from .utils import *


delete_files = True


class VideoToTextFile:
    """Class to extract text from video."""

    def __init__(self):
        """Constructor of VideoToTextFile class."""
        self.stt = SpeechRecognition()

    def video_to_text_file(self,
                           video_file: str,
                           text_saving_path: str = None,
                           delete_after_process: bool = delete_files):
        """Get text file from video's text.

        :param video_file: Path to a video file.
        :param text_saving_path: Path to a saving file.
        :param delete_after_process: 'True' if you don't need to store video and audio files.
        """
        video_file_name = video_file.split(".")[0]

        if text_saving_path is None:
            text_saving_path = f"{video_file_name}.txt"
        audio_saving_path = f"{video_file_name}.mp3"

        video_to_audio(video_file, audio_saving_path)
        extracted_text = self.stt(audio_saving_path)

        write_file(extracted_text, text_saving_path)

        if delete_after_process:
            remove(video_file)
            remove(audio_saving_path)

    def __call__(self,
                 video_file: str,
                 text_saving_path: str = None,
                 delete_after_process: bool = delete_files,
                 *args, **kwargs):
        """Get text file from video's text.

        :param video_file: Path to a video file.
        :param text_saving_path: Path to a saving file.
        :param delete_after_process: 'True' if you don't need to store video and audio files.
        """
        self.video_to_text_file(video_file, text_saving_path, delete_after_process=delete_after_process)


class AudioToTextFile:
    """Class made for extracting text from audio file."""

    def __init__(self):
        """Constructor of AudioToTextFile class."""
        self.stt = SpeechRecognition()

    def audio_to_text_file(self,
                           audio_file: str,
                           text_saving_path: str = None,
                           delete_after_process: bool = delete_files):
        """Get text file from audio file.

        :param audio_file: Path to an audio file.
        :param text_saving_path: Path to a saving file.
        :param delete_after_process: 'True' if you don't need to store audio files.
        """
        audio_file_name = audio_file.split(".")[0]
        if text_saving_path is None:
            text_saving_path = audio_file_name + ".txt"

        extracted_text = self.stt(audio_file=audio_file)

        write_file(file_name=text_saving_path, text=extracted_text)

        if delete_after_process:
            os.remove(audio_file)

    def __call__(self,
                 audio_file: str,
                 text_saving_path: str = None,
                 delete_after_process: bool = delete_files):
        """Get text file from audio file.

        :param audio_file: Path to an audio file.
        :param text_saving_path: Path to a saving file.
        :param delete_after_process: 'True' if you don't need to store audio files.
        """
        return self.audio_to_text_file(audio_file=audio_file,
                                       text_saving_path=text_saving_path,
                                       delete_after_process=delete_after_process)


class VideoAudioToTextFile:
    """Class to extract text from video or audio."""

    def __init__(self):
        """Constructor of VideoAudioToTextFile class."""
        self.stt = SpeechRecognition()

    def video_to_text_file(self,
                           video_file: str,
                           text_saving_path: str = None,
                           delete_after_process: bool = delete_files):
        """Get text file from video's text.

        :param video_file: Path to a video file.
        :param text_saving_path: Path to a saving file.
        :param delete_after_process: 'True' if you don't need to store video and audio files.
        """
        video_file_name = video_file.split(".")[0]

        if text_saving_path is None:
            text_saving_path = f"{video_file_name}.txt"
        audio_saving_path = f"{video_file_name}.mp3"

        video_to_audio(video_file, audio_saving_path)
        extracted_text = self.stt(audio_saving_path)

        write_file(extracted_text, text_saving_path)

        if delete_after_process:
            remove(video_file)
            remove(text_saving_path)

        return extracted_text

    def audio_to_text_file(self,
                           audio_file: str,
                           text_saving_path: str = None,
                           delete_after_process: bool = delete_files):
        """Get text file from audio file.

        :param audio_file: Path to an audio file.
        :param text_saving_path: Path to a saving file.
        :param delete_after_process: 'True' if you don't need to store audio files.
        """
        audio_file_name = audio_file.split(".")[0]
        if text_saving_path is None:
            text_saving_path = audio_file_name + ".txt"

        extracted_text = self.stt(audio_file=audio_file)

        write_file(file_name=text_saving_path, text=extracted_text)

        if delete_after_process:
            remove(text_saving_path)

        return extracted_text
