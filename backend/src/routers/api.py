from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse

router = APIRouter(tags=["Main API"])


@router.get("/", response_class=JSONResponse)
async def index_page(request: Request):
    return {"message": "OK"}
