import os

from fastapi import APIRouter, Request, status
from fastapi.responses import FileResponse, JSONResponse

from exceptions import AIError, APIError
from models import TextItem, VoiceItem
from service.command import CommandHandler
from service.text2speech import TextToSpeech

router = APIRouter(
    tags=["Main API"], prefix="/api", default_response_class=JSONResponse
)


@router.get("/default/{filename}", response_class=FileResponse)
async def get_default_audio(request: Request, filename: str):
    filepath = f"default/{filename}.mp3"
    if not os.path.exists(filepath):
        return JSONResponse(
            {"error": "audiofile not found"}, status_code=status.HTTP_404_NOT_FOUND
        )
    return FileResponse(filepath)


@router.get("/js", response_class=FileResponse)
async def get_javascript(request: Request):
    return FileResponse("component/js/index.js")


@router.post("/command")
async def get_command(request: Request, voice: VoiceItem):
    try:
        command, info = CommandHandler().get_command(voice.voice)
        return {"command": command, "data": info}
    except APIError as e:
        return JSONResponse({"error": str(e)}, status_code=status.HTTP_404_NOT_FOUND)


@router.post("/speech")
async def text_to_speach(request: Request, text: TextItem):
    try:
        content = TextToSpeech().convert(text.text)
        return {"content": content}
    except AIError as e:
        return JSONResponse(
            {"error": str(e)}, status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
