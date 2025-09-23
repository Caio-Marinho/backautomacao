from pydantic_settings import BaseSettings

class Configuration(BaseSettings):
    DATABASE_URL: str
    FUSO_LOCAL:str
    debug: bool = False
    port: int = 5000

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

# Instância global
configuration = Configuration()