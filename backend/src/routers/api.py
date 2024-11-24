from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse

router = APIRouter(tags=["Main API"], prefix="/api")


@router.get("/", response_class=JSONResponse)
async def index_page(request: Request):
    return {"message": "OK"}


@router.post("/command", response_class=JSONResponse)
async def get_command(request: Request):
    return {"message": "OK"}


@router.post("/speach", response_class=JSONResponse)
async def text_to_speach(request: Request):
    return {"message": "OK"}
