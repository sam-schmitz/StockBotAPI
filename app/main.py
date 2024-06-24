#main.py
#By: Sam Schmitz

from fastapi import FastAPI, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from . import crud, models, schemas
from .database import engine, get_db
from typing import List, Optional
from .auth import router as auth_router, get_current_user

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(auth_router, prefix="/auth")
        
@app.post("/members/", response_model=schemas.Member)
def create_member(member: schemas.MemberCreate, db: Session = Depends(get_db),
                current_user: schemas.User = Depends(get_current_user)):
    return crud.create_member(db=db, member=member)

@app.get("/members/{member_id}", response_model=schemas.Member)
def read_member(member_id:int, db:Session = Depends(get_db)):
    db_member = crud.get_member_by_id(db, member_id=member_id)
    if db_member is None:
        raise HTTPException(status_code=404, detail="Member not found")
    return db_member

@app.get("/members/name/{member_name}", response_model=schemas.Member)
def read_member_by_name(member_name: str, db: Session = Depends(get_db)):
    db_member = crud.get_member_by_name(db, name=member_name)
    if db_member is None:
        raise HTTPException(status_code=404, detail="Member not found")
    return db_member

@app.get("/members/", response_model=List[schemas.Member])
def read_members(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    members = crud.get_members(db, skip=skip, limit=limit)
    return members

@app.post("/stocks/", response_model=schemas.Stock)
def create_stock(stock: schemas.StockCreate, db: Session = Depends(get_db),
                current_user: schemas.User = Depends(get_current_user)):
    return crud.create_stock(db=db, stock=stock)

@app.get("/stocks/{stock_id}", response_model=schemas.Stock)
def read_stock(stock_id:int, db: Session = Depends(get_db)):
    db_stock = crud.get_stock_by_id(db, stock_id=stock_id)
    if db_stock is None:
        raise HTTPException(status_code=404, detail="Stock not found")
    return db_stock

@app.get("/stocks/tick/{stock_tick}", response_model=schemas.Stock)
def read_stock_by_tick(stock_tick: str, db: Session = Depends(get_db)):
    db_stock = crud.get_stock_by_tick(db, tick=stock_tick)
    if db_stock is None:
        raise HTTPException(status_code=404, detail="Stock not found")
    return db_stock

@app.get("/stocks/", response_model=List[schemas.Stock])
def read_stocks(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    stocks = crud.get_stocks(db, skip=skip, limit=limit)
    return stocks

@app.post("/trades/", response_model=schemas.Trade)
def create_trade(trade: schemas.TradeCreate, db: Session = Depends(get_db),
                current_user: schemas.User = Depends(get_current_user)):
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

@app.get("/trades/filter/", response_model=List[schemas.Trade])
def read_trades_by_filter(skip: int = 0,
                          limit: int = 10,
                          memberID: Optional[int] = Query(None),
                          stockID: Optional[int] = Query(None),
                          dateBought: Optional[int] = Query(None),
                          dateDisclosed: Optional[int] = Query(None),
                          delay: Optional[int] = Query(None),
                          db: Session = Depends(get_db)):
    trades = crud.get_trades_by_filter(db, skip=skip, limit=limit,
                                       memberID=memberID, stockID=stockID,
                                       dateBought=dateBought,
                                       dateDisclosed=dateDisclosed, delay=delay)
    if not trades:
        raise HTTPException(status_code=404, detail="Trades not found for the given filters")
    return trades

@app.get("/trades/member/{memberID}", response_model=List[schemas.Trade])
def read_trades_by_memberID(memberID: int, db: Session = Depends(get_db)):
    trades = crud.get_trades_by_memberID(db, memberID=memberID)
    if not trades:
        raise HTTPException(status_code=404, detail=f"No trades found for trader_id {memberID}")
    return trades

@app.get("/trades/stock/{stock_id}", response_model=List[schemas.Trade])
def read_trades_by_stockID(stockID: int, db: Session = Depends(get_db)):
    trades = crud.get_trades_by_stockID(db, stockID=stockID)
    if not trades:
        raise HTTPException(status_code=404, detail=f"No trades fond for stock_id {stockID}")
    return trades

@app.post("/newestDate/", response_model=schemas.DateCreate)
def create_newestDate(date:schemas.DateCreate, db: Session = Depends(get_db),
                current_user: schemas.User = Depends(get_current_user)):
    return crud.create_newestDate(db=db, date=date)

@app.get("/newestDate/", response_model=int)
def read_newestDate(db: Session = Depends(get_db)):
    db_newestDate = crud.get_newestDate(db)
    if db_newestDate is None:
        raise HTTPException(status_code=404, detail="Newest Date not Found")
    return db_newestDate

@app.post("/oldestDate/", response_model=schemas.DateCreate)
def create_oldestDate(date: schemas.DateCreate, db: Session = Depends(get_db),
                current_user: schemas.User = Depends(get_current_user)):
    return crud.create_oldestDate(db=db, date=date)

@app.get("/oldestDate/", response_model=int)
def read_oldestDate(db: Session = Depends(get_db)):
    db_oldestDate = crud.get_oldestDate(db)
    if db_oldestDate is None:
        raise HTTPException(status_code=404, detail="Oldest Date not Found")
    return db_oldestDate