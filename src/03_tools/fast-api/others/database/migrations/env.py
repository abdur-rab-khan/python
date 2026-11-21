from app.core.config import settings
from sqlmodel import SQLModel

from ..schema import Hero

config.set_main_option("sqlalchemy.url", settings.DATABASE_URL)
target_metadata = SQLModel.metadata
