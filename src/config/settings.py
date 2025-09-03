from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str
    open_ai_key: str
    huggingface_key: str


    class Config:
        env_file = ".env"

#can cache this
settings = Settings()



def load_system_prompt():
    try:
        with open("src/prompts/systemPrompts.md", "r") as promptFile:
            return promptFile.read()
    except FileNotFoundError:
        return None
system_prompt = load_system_prompt()