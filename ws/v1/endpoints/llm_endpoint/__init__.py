from fastapi import APIRouter
from .brief import router as brief_router
from .chatbot import router as chatnot_router

llm_router = APIRouter(tags=["LLM"])

llm_router.include_router(brief_router, prefix="/brief")
llm_router.include_router(chatnot_router, prefix="/chatbot")
