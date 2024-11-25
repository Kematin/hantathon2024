from pydantic import BaseModel


class VoiceItem(BaseModel):
    # base 64
    voice: str
