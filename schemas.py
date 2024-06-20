#schemas.py
#By: Sam Schmitz

from pydantic import BaseModel
from typing import List, Optional

class MemberBase(BaseModel):
    comittees: str
    name: str
    
class MemberCreate(MemberBase):
    pass

class Member(MemberBase):
    memberID: int
    
    class Config:
        orm_mode = True
        
class StockBase(BaseModel):
    tick: str
    sector: str
    industry: str
    companyName: str
    
class StockCreate(StockBase):
    pass

class Stock(StockBase):
    stockID: int
    
    class Config:
        orm_mode = True
        
class TradeBase(BaseModel):
    saleType: str
    dateBought: int
    priceBought: int
    dateDisclosed: int
    delay: int
    crossover: int
    size: int
    
class TradeCreate(TradeBase):
    pass

class Trade(TradeBase):
    tradeID: int
    
    class Config:
        orm_mode = True
    
