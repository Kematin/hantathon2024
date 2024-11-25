from typing import Literal

from faster_whisper import WhisperModel

model = None


def init_model(type: Literal["cuda", "cpu"] = "cpu"):
    global model
    if model is not None:
        return model
    # model = WhisperModel(model_size, device="cuda", compute_type="float16")
    if type == "cpu":
        model_size = "medium"
        model = WhisperModel(model_size, device="cpu", compute_type="int8")
    return model
