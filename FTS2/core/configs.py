from pydantic import BaseSettings
from sqlalchemy.ext.declarative import declarative_base

class Settings(BaseSettings):
    API_STR: str = '/api/v1'
    DB_URL: str = "postgresql+asyncpg://teste:123456@localhost:5439/postgres"
    DBBaseModel = declarative_base()

    class Config:
        case_sensitive = True

settings = Settings()
