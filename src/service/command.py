from service.speech2text import SpeechToText
from setup.init_model import init_speech_model

base64content = str


class CommandHandler:
    def __init__(self) -> None:
        pass

    def get_command(self, voice: base64content):
        model = init_speech_model()
        text = SpeechToText(model).convert(voice)
        return text
