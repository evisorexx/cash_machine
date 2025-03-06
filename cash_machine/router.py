from fastapi import APIRouter
from .modules.routers import cash_machine, media


api_router = APIRouter()

api_router.include_router(cash_machine.router)
api_router.include_router(media.router)