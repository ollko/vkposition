from sqlalchemy import create_engine

from fastapi_app.config import settings

engine = create_engine(url=settings.pg_url, echo=False)
