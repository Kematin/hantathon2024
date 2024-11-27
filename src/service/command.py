from typing import Dict, Tuple

from loguru import logger

from service.speech2text import SpeechToText
from setup.init_model import init_hmao_model, init_speech_model

base64content = str

additional_info = Dict | None


class CommandHandler:
    def __init__(self) -> None:
        pass

    def __get_text(self, voice: base64content):
        model = init_speech_model()
        text = SpeechToText(model).convert(voice)
        text = (
            text.replace("\n", " ")
            .replace(".", "")
            .replace(",", "")
            .replace("!", "")
            .replace("?", "")
            .strip()
        )
        return text

    def __get_additional_info(self, command: str, text: str) -> additional_info:
        return {"place": "Белый яр"}

    def convert_text_to_command(self, text: str) -> Tuple[str, additional_info]:
        model = init_hmao_model()
        command = model(text)[0]["label"]
        additional_info = self.__get_additional_info(command, text)
        return command, additional_info

    def get_command(self, voice: base64content) -> Tuple[str, additional_info]:
        text = self.__get_text(voice)
        logger.debug(text)
        command, info = self.convert_text_to_command(text)
        return command, info
