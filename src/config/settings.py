from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str
    open_ai_key: str
    huggingface_key: str

    class Config:
        env_file = ".env"

#can cache this
settings = Settings()

