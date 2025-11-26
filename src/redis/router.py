from fastapi import APIRouter
from src.redis.session import redis_client

router = APIRouter()

@router.post("/set")
async def set_value(key: str, value: str):
    await redis_client.set(key, value)
    return {"status": "saved", "key": key, "value": value}

@router.get("/get/{key}")
async def get_value(key: str):
    value = await redis_client.get(key)
    return {"key": key, "value": value}
