from contextlib import asynccontextmanager

from fastapi import FastAPI

from backend.core.logging import logger


@asynccontextmanager
async def lifespan(app: FastAPI):

    logger.info("Starting AI Software Architecture Reviewer")

    yield

    logger.info("Stopping AI Software Architecture Reviewer")