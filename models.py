
#models.py
#By: Sam Schmitz

from sqlalchemy import Column, Integer, String, Float, ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

DATABASE_URL = "sqlite:///./sbDatabase.db"

Base = declarative_base()

class Member(Base):
    __tablename__ = "members"
    memberID = Column(Integer, primary_key=True, index=True)
    comittees = Column(String, index=True)
    name = Column(String, index=True)

class Stock(Base):
    __tablename__ = "stocks"
    stockID = Column(Integer, primary_key=True, index=True)
    tick = Column(String, index=True)
    sector = Column(String, index=True)
    industry = Column(String, index=True)
    CompnayName = Column(String, index=True)
    
class Trade(Base):
    __tablename__ = "trades"
    tradeID = Column(Integer, primary_key=True, index=True)
    stockID = Column(Integer, ForeignKey('stocks.stockID'))
    saleType = Column(String, index=True)
    memberID = Column(Integer, ForeignKey('members.membersID'))
    dateBought = Column(Integer, index=True)
    priceBought = Column(Float)
    dateDisclosed = Column(Integer, index=True)
    delay = Column(Integer)
    crossover = Column(Integer)
    size = Column(Integer)
    
    stock = relationship("Stock")
    member = relationship("Member")
    
    
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread":False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    
Base.metadata.create_all(bind=engine)