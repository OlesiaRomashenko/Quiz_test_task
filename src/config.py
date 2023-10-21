from pydantic_settings import BaseSettings, SettingsConfigDict

class SettingsDB(BaseSettings):
    engine: str
    host: str
    port: str
    db: str
    user: str
    password: str
    model_config = SettingsConfigDict(env_prefix="POSTGRES_", env_file="./.env")


class Settings(BaseSettings):
    title: str
    summary: str
    description: str
    docs_url: str
    model_config = SettingsConfigDict(env_prefix="API_", env_file="./.env")


