#main.py
#By: Sam Schmitz

from urllib import response
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import crud, models, schemas
from .database import SessionLocal, engine
from typing import List, Optional

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
@app.post("/members/", response_model=schemas.Member)
def create_member(member: schemas.MemberCreate, db: Session = Depends(get_db)):
    return crud.create_member(db=db, member=member)

@app.get("/members/{member_id}", response_model=schemas.Member)
def read_member(member_id:int, db:Session = Depends(get_db)):
    db_member = crud.get_member(db, member_id=member_id)
    if db_member is None:
        raise HTTPException(status_code=404, detail="Member not found")
    return db_member

@app.get("/members/", response_model=List[schemas.Member])
def read_members(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    members = crud.get_members(db, skip=skip, limit=limit)
    return members

@app.post("/stocks/", response_model=schemas.Stock)
def create_stock(stock: schemas.StockCreate, db: Session = Depends(get_db)):
    return crud.create_stock(db=db, stock=stock)

@app.get("/stocks/{stock_id}", response_model=schemas.Stock)
def read_stock(stock_id:int, db: Session = Depends(get_db)):
    db_stock = crud.get_stock(db, stock_id=stock_id)
    if db_stock is None:
        raise HTTPException(status_code=404, detail="Stock not found")
    return db_stock

@app.get("/stocks/", response_model=List[schemas.Stock])
def read_stocks(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    stocks = crud.get_stocks(db, skip=skip, limit=limit)
    return stocks

@app.post("/trades/", response_model=schemas.Trade)
def create_trade(trade: schemas.TradeCreate, db: Session = Depends(get_db)):
    return crud.create_trade(db=db, trade=trade)

@app.get("/trade/{trade_id}", response_model=schemas.Trade)
def read_trade(trade_id: int, db: Session = Depends(get_db)):
    db_trade = crud.get_trade(db, trade_id=trade_id)
    if db_trade is None:
        raise HTTPException(status_code=404, detail="Trade not Found")
    return db_trade

@app.get("/trades/", response_model=List[schemas.Trade])
def read_trades(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    trades = crud.get_trades(db, skip=skip, limit=limit)
    return trades

@app.get("/newestDate/", response_model=schemas.NewestDate)
def read_newestDate(db: Session = Depends(get_db)):
    db_newestDate = crud.get_newestDate(db)
    if db_newestDate is None:
        raise HTTPException(status_code=404, detail="Newest Date not Found")
    return db_newestDate

@app.get("/oldestDate/", response_model=schemas.OldestDate)
def read_oldestDate(db: Session = Depends(get_db)):
    db_oldestDate = crud.get_oldestDate(db)
    if db_oldestDate is None:
        raise HTTPException(status_code=404, detail="Oldest Date not Found")
    return db_oldestDate