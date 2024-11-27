from time import time
from typing import Literal

from faster_whisper import WhisperModel
from loguru import logger
from transformers import pipeline

model = None
classifier = None


def init_speech_model(device: Literal["cuda", "cpu"] = "cpu") -> WhisperModel:
    global model
    if model is not None:
        return model
    model_size = "medium"
    start = time()
    if device == "cpu":
        model = WhisperModel(model_size, device="cpu", compute_type="int8")
    if device == "cuda":
        model = WhisperModel(model_size, device="cuda", compute_type="float16")
    end = time()
    logger.info(f"INIT WHISPER {device} AI MODEL AT {end-start:.2f} s.")
    return model


def init_hmao_model(model: str = "ai_hmao_model") -> pipeline:
    global classifier
    if classifier is not None:
        return classifier

    start = time()
    classifier = pipeline("text-classification", model)
    end = time()
    logger.info(f"INIT HMAO AI MODEL {end-start:.2f} s.")
    return classifier
