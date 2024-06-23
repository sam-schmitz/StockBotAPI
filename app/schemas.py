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
    memberID: int
    stockID: int
    saleType: str
    dateBought: int
    priceBought: float
    dateDisclosed: int
    priceDisclosed: float
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
    
class DateCreate(DateBase):
    pass
    
class NewestDate(DateBase):
    pass
    
class OldestDate(DateBase):
    pass

class User(BaseModel):
    username: str
    
    class Config:
        orm_mode = True
        
class UserCreate(User):
    password: str
    
class Token(BaseModel):
    access_token: str
    token_type: str
    
class TokenData(BaseModel):
    username: str | None = None
    
