from fastapi import APIRouter, Request
from fastapi.responses import FileResponse, JSONResponse

router = APIRouter(tags=["Main API"], prefix="/api")


@router.get("/", response_class=JSONResponse)
async def index_page(request: Request):
    return {"message": "OK"}


@router.get("/js", response_class=FileResponse)
async def get_javascript(request: Request):
    return FileResponse("component/js/index.js")


@router.post("/command", response_class=JSONResponse)
async def get_command(request: Request):
    return {"message": "OK"}


@router.post("/speach", response_class=JSONResponse)
async def text_to_speach(request: Request):
    return {"message": "OK"}
