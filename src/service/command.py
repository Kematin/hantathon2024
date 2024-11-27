from typing import Dict, Literal, Tuple

from loguru import logger

from exceptions import APIError
from service.speech2text import SpeechToText
from setup.init_model import init_hmao_model, init_speech_model

base64content = str

additional_info = Dict | None


class CommandHandler:
    static_commands = ["site_info", "legend_info", "open_card", "disability_group"]
    dynamic_commands = [
        "path",
        "legend_place",
        "search_radius",
        "detailed_info",
        "search_place",
    ]
    commands = static_commands + dynamic_commands

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

    def __get_additional_info(
        self,
        command: Literal[
            "site_info",
            "legend_info",
            "open_card",
            "disability_group",
            "path",
            "legend_place",
            "search_radius",
            "detailed_info",
            "search_place",
        ],
        text: str,
    ) -> additional_info:
        if command in self.static_commands:
            return None

        stop_words = [
            "до",
            "д",
            "адрес",
            "адресс",
            "к",
            "в",
            "рядом",
            "легенда",
            "легенду",
            "легенд",
            "районе",
            "район",
            "тут",
            "город",
            "города",
            "городе",
            "поселок",
            "поселка",
            "поселке",
            "радиус",
            "радиуса",
            "радиусе",
            "мне",
            "объект",
            "объекта",
            "карте",
            "карта",
            "не",
        ]
        place = None
        words = text.split()
        for i, word in enumerate(words):
            if word in stop_words:
                place = " ".join(words[i + 1 :])
        if place is None:
            return None
        else:
            return {"place": place}

    def convert_text_to_command(self, text: str) -> Tuple[str, additional_info]:
        model = init_hmao_model()
        result = model(text)[0]
        command, score = result["label"], result["score"]
        if score < 0.5:
            raise APIError("Command not found")
        additional_info = self.__get_additional_info(command, text)
        return command, additional_info

    def get_command(self, voice: base64content) -> Tuple[str, additional_info]:
        text = self.__get_text(voice)
        logger.debug(text)
        command, info = self.convert_text_to_command(text)
        return command, info
