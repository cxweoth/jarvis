from fastapi import Request
from pydantic import BaseModel
from fastapi import APIRouter, HTTPException, Request, Query, Response, Depends
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional

from cfg import Config

router = APIRouter()

class BriefResponse(BaseModel):
    Org: str
    Product: str
    APIType: str
    SpeakerType: str

@router.get("", response_model=BriefResponse)
def get_brief_api(request: Request):
    config: Config = request.app.state.config
    return BriefResponse(Org="CXWEO", Product="Jarvis", APIType='LLM', SpeakerType=config.speaker_type)
