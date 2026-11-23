from fastapi import FastAPI

from backend.app.config.settings import settings
from backend.app.config.logging_config import setup_logging, logger
from backend.app.middleware.error_handler import global_exception_handler
from backend.app.config.langsmith import configure_langsmith
from backend.app.api.documents import router as document_router
from backend.app.api.chunks import router as chunk_router
from backend.app.api.embeddings import router as embedding_router
from backend.app.api.evidence import router as evidence_router
from backend.app.api import retrieval

# Initialize logging first
setup_logging()

# Configure LangSmith tracing
configure_langsmith()


# Create FastAPI application
app = FastAPI(title=settings.APP_NAME,version=settings.APP_VERSION)

# Register exception handler
app.add_exception_handler(Exception,global_exception_handler)

# Register API routers
app.include_router(document_router)
app.include_router(chunk_router)
app.include_router(embedding_router)
app.include_router(evidence_router)
app.include_router(retrieval.router)

@app.get("/")
def health_check():

    logger.info("Health check executed")

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