from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = "TTB Label Verification Prototype"
    BACKEND_CORS_ORIGINS: list[str] = [
        "http://localhost:5173",
    ]

settings = Settings()