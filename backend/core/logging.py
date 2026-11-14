from pathlib import Path

from loguru import logger

from backend.core.settings import settings

Path("logs").mkdir(exist_ok=True)

logger.remove()

logger.add(
    settings.LOG_PATH,
    level=settings.LOG_LEVEL,
    rotation="10 MB",
    retention="30 days",
    enqueue=True,
    backtrace=True,
    diagnose=True,
)

logger.add(
    sink=lambda msg: print(msg, end=""),
    level=settings.LOG_LEVEL,
)