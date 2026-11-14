from fastapi import FastAPI

from backend.api.router import api_router
from backend.core.constants import APP_DESCRIPTION
from backend.core.lifespan import lifespan
from backend.core.settings import settings

app = FastAPI(
    title=settings.APP_NAME,
    description=APP_DESCRIPTION,
    version=settings.APP_VERSION,
    lifespan=lifespan,
)

app.include_router(api_router)


@app.get("/", tags=["Root"])
async def root():

    return {
        "application": settings.APP_NAME,
        "version": settings.APP_VERSION,
        "environment": settings.ENVIRONMENT,
        "status": "running",
    }