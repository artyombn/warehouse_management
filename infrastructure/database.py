from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .orm import Base

DATABASE_URL = 'sqlite:///warehouse.db'

