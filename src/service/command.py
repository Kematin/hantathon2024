from io import BytesIO
from time import time

from faster_whisper import WhisperModel


class SpeechToText:
    def __init__(self) -> None:
        pass

    def convert(self, file_content: BytesIO, lang: str = "ru") -> str:
        model_size = "medium"
        # model = WhisperModel(model_size, device="cuda", compute_type="float16")

        start = time()
        model = WhisperModel(model_size, device="cpu", compute_type="int8")
        end = time()
        print(f"[LOG]: Init model: {end-start} s.")
        start = time()
        segments, info = model.transcribe(file_content, beam_size=5, language="ru")
        end = time()
        print(f"[LOG]: Get segments: {end-start} s.")

        total_text = ""
        i = 1
        for segment in segments:
            start = time()
            total_text += "[%.2fs -> %.2fs] %s\n" % (
                segment.start,
                segment.end,
                segment.text,
            )
            end = time()
            print(f"[LOG]: Get segment {i}: {end-start} s.")
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
