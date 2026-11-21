from fastapi import FastAPI

from backend.api.router import api_router
from backend.core.constants import APP_DESCRIPTION
from backend.core.lifespan import lifespan
from backend.core.settings import settings
from backend.api.v1.upload import router as upload_router

app = FastAPI(
    title=settings.APP_NAME,
    description=APP_DESCRIPTION,
    version=settings.APP_VERSION,
    lifespan=lifespan,
)

app.include_router(
    upload_router,
    prefix="/api/v1",
)


@app.get("/", tags=["Root"])
async def root():

    return {
        "application": settings.APP_NAME,
        "version": settings.APP_VERSION,
        "environment": settings.ENVIRONMENT,
        "status": "running",
    }