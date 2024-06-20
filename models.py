
#models.py
#By: Sam Schmitz


from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///./sbDatabase.db"

Base = declarative_base()