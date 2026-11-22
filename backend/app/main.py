from fastapi import FastAPI

from backend.app.config.settings import settings
from backend.app.config.logging_config import setup_logging, logger
from backend.app.middleware.error_handler import (global_exception_handler)
from backend.app.config.langsmith import configure_langsmith


configure_langsmith()

setup_logging()


app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION
)


app.add_exception_handler(
    Exception,
    global_exception_handler
)


@app.get("/")
def health_check():

    logger.info(
        "Health check executed"
    )

    return {
        "application": settings.APP_NAME,
        "version": settings.APP_VERSION,
        "status": "running"
    }


@app.get("/health")
def health():

    return {
        "status": "healthy"
    }