import os
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

from cfg import Config

def get_web_app(config: Config):
    web_app = FastAPI()

    web_app.mount("/static", StaticFiles(directory=config.web_path), name="static")
    @web_app.get("/")
    async def read_root():
        return FileResponse(os.path.join(config.web_path, "index.html"))
    return web_app

