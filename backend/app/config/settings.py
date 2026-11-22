from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    APP_NAME: str
    APP_VERSION: str
    ENVIRONMENT: str

    LOG_LEVEL: str

    HOST: str
    PORT: int


    class Config:
        env_file = ".env"


settings = Settings()