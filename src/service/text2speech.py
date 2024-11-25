import base64
import tempfile

from gtts import gTTS

base64content = str


class TextToSpeech:
    def __init__(self) -> None:
        pass

    def convert(self, text: str, lang: str = "ru", save: bool = False) -> base64content:
        myobj = gTTS(text=text, lang=lang, slow=False)

        content = None
        with tempfile.NamedTemporaryFile(suffix=".mp3", delete=True) as temp_file:
            if save:
                myobj.save("speech_test.mp3")
            myobj.save(temp_file.name)

            with open(temp_file.name, "rb") as file:
                content = file.read()

            file.close()

        base64_string = base64.b64encode(content).decode("utf-8")
        return base64_string
