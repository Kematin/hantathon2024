import base64
from io import BytesIO
from time import time

from faster_whisper import WhisperModel
from loguru import logger


class SpeechToText:
    def __init__(self, model: WhisperModel) -> None:
        self.model = model

    def __get_bytes(self, content: BytesIO | bytes | str) -> BytesIO:
        if type(content) is bytes:
            content = BytesIO(content)
        elif type(content) is str:
            file_data = content.encode()
            content = base64.b64decode(file_data)
            content = BytesIO(content)

        return content

    def convert(self, file_content: BytesIO | bytes | str, lang: str = "ru") -> str:
        file_content = self.__get_bytes(file_content)

        segments, info = self.model.transcribe(file_content, beam_size=5, language="ru")

        total_text = ""
        i = 1
        for segment in segments:
            start = time()
            total_text += segment.text + "\n"
            end = time()
            logger.debug(f"[LOG]: Get segment {i}: {end-start} s.")
            i += 1

        return total_text

    def get_file_content(self, filename: str) -> BytesIO:
        with open(filename, "rb") as file:
            file_content = BytesIO(file.read())
            return file_content


if __name__ == "__main__":
    speach = SpeechToText()
    filename = "test.mp3"
    file_content = speach.get_file_content(filename)
    result = speach.convert(file_content)
    print(result)
