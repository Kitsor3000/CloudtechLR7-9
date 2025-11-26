from fastapi import APIRouter
from src.external_api.service import ExternalService

router = APIRouter()

@router.get("/cat")
async def get_cat():
    return await ExternalService.get_cat()
