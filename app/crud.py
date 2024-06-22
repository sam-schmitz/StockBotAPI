#crud.py
#By: Sam Schmitz

from sqlalchemy.orm import Session
from sqlalchemy.sql import func
from . import models, schemas

def get_member_by_id(db: Session, member_id:int):
    return db.query(models.Member).filter(models.Member.memberID == member_id).first()

def get_member_by_name(db: Session, name: str):
    return db.query(models.Member).filter(models.Member.name == name).first()

def get_members(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Member).offset(skip).limit(limit).all()

def create_member(db: Session, member:schemas.MemberCreate):
    db_member = models.Member(comittees=member.comittees, 
                              name=member.name)
    db.add(db_member)
    db.commit()
    db.refresh(db_member)
    return db_member

def get_stock_by_id(db: Session, stock_id: int):
    return db.query(models.Stock).filter(models.Stock.stockID == stock_id).first()

def get_stock_by_tick(db: Session, tick: str):
    return db.query(models.Stock).filter(models.Stock.tick == tick).first()

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


def get_trades_by_filter(db: Session, skip: int = 0, limit: int = 10,
                         memberID: int = None, stockID: int = None,
                         dateBought: int = None, dateDisclosed: int = None,
                         delay: int = None):
    q = db.query(models.Trade)
    if memberID:
        q = q.filter(models.Trade.memberID == memberID)
    if stockID:
        print(f"filtering for stockID {stockID}")
        q = q.filter(models.Trade.stockID == stockID)
    if dateBought:
        q = q.filter(models.Trade.dateBought == dateBought)
    if dateDisclosed:
        q = q.filter(models.Trade.dateDisclosed == dateDisclosed)
    if delay:
        q = q.filter(models.Trade.delay == delay)
    return q.offset(skip).limit(limit).all()

def get_trades_by_memberID(db: Session, memberID: int):
    return db.query(models.Trade).filter(models.Trade.memberID == memberID).all()

def get_trades_by_stockID(db: Session, stockID: int):
    return db.query(models.Trade).filter(models.Trade.stockID == stockID).all()

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

def create_newestDate(db: Session, date:schemas.DateCreate):
    db_newestDate = models.NewestDate(date=date.date)
    db.add(db_newestDate)
    db.commit()
    db.refresh(db_newestDate)
    return db_newestDate

def get_oldestDate(db: Session):
    return db.query(func.min(models.OldestDate.date)).scalar()

def create_oldestDate(db: Session, date:schemas.DateCreate):
    db_oldestDate = models.OldestDate(date=date.date)
    db.add(db_oldestDate)
    db.commit()
    db.refresh(db_oldestDate)
    return db_oldestDate