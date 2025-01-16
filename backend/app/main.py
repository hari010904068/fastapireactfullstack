from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import crud, models, schemas, database

app = FastAPI()

# Dependency
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/accounts/")
def create_account(name: str, db: Session = Depends(get_db)):
    return crud.create_account(db=db, name=name)

@app.get("/accounts/{account_id}")
def read_account(account_id: int, db: Session = Depends(get_db)):
    account = crud.get_account(db, account_id=account_id)
    if account is None:
        raise HTTPException(status_code=404, detail="Account not found")
    return account

@app.post("/accounts/{account_id}/deposit")
def deposit(account_id: int, amount: float, db: Session = Depends(get_db)):
    account = crud.deposit(db, account_id=account_id, amount=amount)
    if account is None:
        raise HTTPException(status_code=404, detail="Account not found or insufficient funds")
    return account

@app.post("/accounts/{account_id}/withdraw")
def withdraw(account_id: int, amount: float, db: Session = Depends(get_db)):
    account = crud.withdraw(db, account_id=account_id, amount=amount)
    if account is None:
        raise HTTPException(status_code=404, detail="Account not found or insufficient funds")
    return account

@app.get("/accounts/{account_id}/transactions")
def get_transactions(account_id: int, skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_transactions(db, account_id=account_id, skip=skip, limit=limit)
