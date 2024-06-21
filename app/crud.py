#crud.py
#By: Sam Schmitz

from sqlalchemy.orm import Session
from sqlalchemy.sql import func
from . import models, schemas

def get_member(db: Session, member_id:int):
    return db.query(models.Member).filter(models.Member.memberID == member_id).first()

def get_members(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Member).offset(skip).limit(limit).all()

def create_member(db: Session, member:schemas.MemberCreate):
    db_member = models.Member(comittees=member.comittees, 
                              name=member.name)
    db.add(db_member)
    db.commit()
    db.refresh(db_member)
    return db_member

def get_stock(db: Session, stock_id: int):
    return db.query(models.Stock).filter(models.Stock.stockID == stock_id).first()

def get_stocks(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Stock).offset(skip).limit(limit).all()

def create_stock(db: Session, stock:schemas.StockCreate):
    db_stock = models.Stock(tick=stock.tick,
                            sector=stock.sector,
                            industry=stock.industry,
                            companyName=stock.companyName)
    db.add(db_stock)
    db.commit()
    db.refresh(db_stock)
    return db_stock

def get_trade(db: Session, trade_id:int):
    return db.query(models.Trade).filter(models.Trade.tradeID == trade_id).first()

def get_trades(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Trade).offset(skip).limit(limit).all()

def create_trade(db: Session, trade:schemas.TradeCreate):
    db_trade = models.Trade(saleType=trade.saleType, 
                            dateBought=trade.dateBought,
                            priceBought=trade.priceBought,
                            dateDisclosed=trade.dateDisclosed,
                            delay=trade.delay,
                            crossover=trade.crossover,
                            size=trade.size)
    db.add(db_trade)
    db.commit()
    db.refresh(db_trade)
    return db_trade

def get_newestDate(db: Session):
    return db.query(func.max(models.NewestDate.date)).scalar()

def get_oldestDate(db: Session):
    return db.query(func.min(models.OldestDate.date)).scalar()

