from moviepy.editor import VideoFileClip


def video_to_audio(mp4file: str, mp3file: str):
    video = VideoFileClip(mp4file)
    audio = video.audio
    audio.write_audiofile(mp3file)
    audio.close()
    video.close()


def write_file(text: str, file_name: str):
    with open(file_name, "w") as pfd_file:
        pfd_file.write(text)
