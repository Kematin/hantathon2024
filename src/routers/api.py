from fastapi import APIRouter, Request
from fastapi.responses import FileResponse, JSONResponse
from loguru import logger

from models import TextItem, VoiceItem
from service.command import CommandHandler
from service.text2speech import TextToSpeech

router = APIRouter(tags=["Main API"], prefix="/api")


@router.get("/", response_class=JSONResponse)
async def index_page(request: Request):
    return {"message": "OK"}


@router.get("/js", response_class=FileResponse)
async def get_javascript(request: Request):
    return FileResponse("component/js/index.js")


@router.post("/command", response_class=JSONResponse)
async def get_command(request: Request, voice: VoiceItem):
    command = CommandHandler().get_command(voice.voice)
    logger.debug(command)
    return {"command": command}


@router.post("/speech", response_class=JSONResponse)
async def text_to_speach(request: Request, text: TextItem):
    content = TextToSpeech().convert(text.text, save=True)
    return {"content": content}
