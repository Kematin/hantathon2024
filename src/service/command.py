from service.speech2text import SpeechToText

bytes64 = str

from setup.init_model import init_model


class CommandHandler:
    def __init__(self) -> None:
        pass

    def get_command(self, voice: bytes64):
        model = init_model()
        text = SpeechToText(model).convert(voice)
        return text
