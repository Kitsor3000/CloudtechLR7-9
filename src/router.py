import logging

from fastapi import APIRouter, HTTPException

router = APIRouter(prefix="/api")

logger = logging.getLogger(__name__)


@router.get("/health")
def healthcheck():
    logger.info("Healthcheck OK")
    return {"status": "ok"}


@router.get("/error")
def generate_error():
    logger.error("Manual error triggered")
    raise HTTPException(500, "Test error for CI/Sentry")
