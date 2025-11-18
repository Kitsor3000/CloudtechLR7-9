from fastapi import FastAPI

from src.external_api.router import router as external_router

app = FastAPI(
    title="Azure Storage + External API",
    version="0.1.0"
)


app.include_router(external_router)       # наш новий модуль

@app.get("/")
def root():
    return {"message": "App is running"}
