#schemas.py
#By: Sam Schmitz

from pydantic import BaseModel
from typing import List, Optional

class MemberBase(BaseModel):
    comittees: Optional[str] = None
    name: str
    
class MemberCreate(MemberBase):
    pass

class Member(MemberBase):
    memberID: int
    
    class Config:
        from_attributes = True
        
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
        from_attributes = True
        
class TradeBase(BaseModel):
    saleType: str
    dateBought: int
    priceBought: float
    dateDisclosed: int
    delay: int
    crossover: Optional[int] = None
    size: int
    
class TradeCreate(TradeBase):
    pass

class Trade(TradeBase):
    tradeID: int
    
    class Config:
        from_attributes = True
        
class DateBase(BaseModel):
    date: int
    
class NewestDate(DateBase):
    pass
    
class OldestDate(DateBase):
    pass
    
