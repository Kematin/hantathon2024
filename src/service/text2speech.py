import base64
import tempfile

from gtts import gTTS
from gtts.tts import gTTSError
from loguru import logger

# from exceptions import AIError

base64content = str


class TextToSpeech:
    def __init__(self) -> None:
        pass

    def __get_content(self, translate_obj: gTTS, save: bool):
        content = None

        with tempfile.NamedTemporaryFile(suffix=".mp3", delete=True) as temp_file:
            if save:
                translate_obj.save("speech_test.mp3")
            translate_obj.save(temp_file.name)

            with open(temp_file.name, "rb") as file:
                content = file.read()

            file.close()

        return content

    def convert(self, text: str, lang: str = "ru", save: bool = False) -> base64content:
        try:
            translate_obj = gTTS(text=text, lang=lang, slow=False)
            content = self.__get_content(translate_obj, save)
            base64_string = base64.b64encode(content).decode("utf-8")
            return base64_string
        except gTTSError as e:
            logger.error(e)
            # raise AIError("Internal AI Error")


if __name__ == "__main__":
    with open("text.txt", "r") as file:
        text = "\n".join(file.readlines())
    TextToSpeech().convert(text, save=True)
