from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi

from cfg import Config
from .endpoints import llm_router

def custom_openapi(api_app: FastAPI, ws_name, version, description):

    if api_app.openapi_schema:
        return api_app.openapi_schema
    
    openapi_schema = get_openapi(
        title=ws_name,
        version=version,
        description=description,
        routes=api_app.routes,
    )

    api_v1_prefix = f'/api/{version}'
    for path in list(openapi_schema["paths"].keys()):
        openapi_schema["paths"][api_v1_prefix + path] = openapi_schema["paths"].pop(path)
    
    api_app.openapi_schema = openapi_schema
    return api_app.openapi_schema

def get_api_v1_app(config: Config):
    api_v1 = FastAPI()
    api_v1.state.config = config
    description = f"{config.ws_name} API v1"
    api_v1.openapi = lambda: custom_openapi(api_v1, config.ws_name, "v1", description)

    api_v1.include_router(llm_router, prefix="/llm")

    return api_v1

