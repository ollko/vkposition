import os
from pydantic_settings import BaseSettings


POSTGRES_URL = os.getenv('POSTGRES_URL')

print(f'{POSTGRES_URL=}')


class Settings(BaseSettings):
    pg_url: str = POSTGRES_URL


settings = Settings()
