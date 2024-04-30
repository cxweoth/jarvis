# Web service
import os
import uvicorn
from cfg import Config
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from ws import get_api_v1_app, get_web_app


def web_service(root_path):

    # get config
    config = Config(root_path)
    host = config.ws_host
    port = config.ws_port

    # set web service
    app = FastAPI()
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
        expose_headers=["X-Total-Count"]
    )
    app.mount("/api/v1", get_api_v1_app(config))
    app.mount("/", get_web_app(config))

    # run web service
    uvicorn.run(app, host=host, port=port)

if __name__ == '__main__':
    root_path = os.path.dirname(os.path.realpath(__file__))
    web_service(root_path)
