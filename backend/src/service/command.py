import io

import speech_recognition as sr
from speech_recognition import AudioFile


class SpeachToText:
    def __init__(self) -> None:
        self.r = sr.Recognizer()

    def convert(self, file_content: bytes) -> str:
        audio_stream = io.BytesIO(file_content)
        print(audio_stream)

        with AudioFile(audio_stream) as source:
            audio_data = self.r.record(source)

        text = self.r.recognize_google_cloud(audio_data)
        return text

    def get_file_content(self, filename: str) -> bytes:
        with open(filename, "rb") as file:
            return file.read()


if __name__ == "__main__":
    speach = SpeachToText()
    filename = "test.mp3"
    file_content = speach.get_file_content(filename)
    result = speach.convert(file_content)
    print(result)
