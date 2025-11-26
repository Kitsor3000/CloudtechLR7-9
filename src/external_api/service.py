import httpx
from src.redis.session import redis_client

class ExternalService:

    @staticmethod
    async def get_cat():
        cached = await redis_client.get("cat_cached")

        if cached:
            return {"cached": True, "data": eval(cached)}

        async with httpx.AsyncClient() as client:
            fact = (await client.get("https://catfact.ninja/fact")).json()
            img = (await client.get("https://api.thecatapi.com/v1/images/search")).json()

        result = {"fact": fact, "image": img}

        await redis_client.set("cat_cached", str(result), ex=30)  # TTL 30 sec

        return {"cached": False, "data": result}
