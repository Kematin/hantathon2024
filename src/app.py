from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from config import config
from routers import routers
from setup import configure_logger, init_speech_model


@asynccontextmanager
async def lifespan(app: FastAPI):
    configure_logger()
    init_speech_model()
    yield


app = FastAPI(lifespan=lifespan)

for route in routers:
    app.include_router(route)


app.add_middleware(
    CORSMiddleware,
    allow_origins=config.origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == "__main__":
    uvicorn.run("app:app", host=config.host, port=config.port, reload=True)
