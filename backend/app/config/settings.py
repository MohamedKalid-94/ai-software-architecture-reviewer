from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):

    # Application
    APP_NAME: str
    APP_VERSION: str
    ENVIRONMENT: str


    # Logging
    LOG_LEVEL: str = "INFO"


    # Backend
    HOST: str = "0.0.0.0"
    PORT: int = 8000


    # Frontend
    BACKEND_URL: str


    # LLM Configuration
    LLM_PROVIDER: str
    LLM_MODEL: str
    OLLAMA_BASE_URL: str

    LLM_TEMPERATURE: float = 0.1
    MAX_TOKENS: int = 2048


    # Embedding Configuration
    EMBEDDING_PROVIDER: str
    EMBEDDING_MODEL: str


    # LangSmith
    LANGSMITH_API_KEY: str = ""
    LANGSMITH_PROJECT: str = "ArchAI Reviewer"
    LANGSMITH_TRACING: bool = False


    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=True,
        extra="ignore"
    )


settings = Settings()