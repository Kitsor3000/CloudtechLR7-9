import sentry_sdk
from fastapi import FastAPI

from src.logging_config import setup_logging
from src.router import router
from src.settings import settings


def create_app() -> FastAPI:
    setup_logging()

    # Init Sentry
    if settings.SENTRY_DSN:
        sentry_sdk.init(
            dsn=settings.SENTRY_DSN,
            traces_sample_rate=1.0,
            send_default_pii=True,
        )

    app = FastAPI(title="FastAPI Labs 16-22 Minimal")

    app.include_router(router)

    return app


app = create_app()
