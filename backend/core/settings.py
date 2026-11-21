from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):

    APP_NAME: str
    APP_VERSION: str
    ENVIRONMENT: str
    DEBUG: bool

    HOST: str
    PORT: int

    LOG_LEVEL: str
    LOG_PATH: str

    OPENAI_API_KEY: str = ""
    GOOGLE_API_KEY: str = ""

    TEMPERATURE: float
    MAX_TOKENS: int

    LLM_PROVIDER: str
    LLM_MODEL: str

    EMBEDDING_PROVIDER: str
    EMBEDDING_MODEL: str

    LANGCHAIN_TRACING_V2: bool
    LANGCHAIN_ENDPOINT: str
    LANGCHAIN_API_KEY: str = ""
    LANGCHAIN_PROJECT: str

    UPLOAD_DIR: str = "backend/storage/uploads"
    MAX_UPLOAD_SIZE_MB: int = 20
    ALLOWED_EXTENSIONS: str = "pdf"

    CHUNK_SIZE: int = 1000
    CHUNK_OVERLAP: int = 200

    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=True,
        extra="ignore",
    )


@lru_cache
def get_settings():
    return Settings()


settings = get_settings()