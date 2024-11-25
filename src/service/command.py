from service.speech2text import SpeechToText
from setup.init_model import init_speech_model

bytes64 = str


class CommandHandler:
    def __init__(self) -> None:
        pass

    def get_command(self, voice: bytes64):
        model = init_speech_model()
        text = SpeechToText(model).convert(voice)
        return text
