from sqlalchemy.orm import Session
from . import models, schemas

def create_account(db: Session, name: str):
    db_account = models.Account(name=name)
    db.add(db_account)
    db.commit()
    db.refresh(db_account)
    return db_account

def get_account(db: Session, account_id: int):
    return db.query(models.Account).filter(models.Account.id == account_id).first()

def deposit(db: Session, account_id: int, amount: float):
    account = db.query(models.Account).filter(models.Account.id == account_id).first()
    if account:
        account.balance += amount
        db.add(models.Transaction(account_id=account_id, transaction_type="deposit", amount=amount))
        db.commit()
        db.refresh(account)
        return account
    return None

def withdraw(db: Session, account_id: int, amount: float):
    account = db.query(models.Account).filter(models.Account.id == account_id).first()
    if account and account.balance >= amount:
        account.balance -= amount
        db.add(models.Transaction(account_id=account_id, transaction_type="withdrawal", amount=amount))
        db.commit()
        db.refresh(account)
        return account
    return None

def get_transactions(db: Session, account_id: int, skip: int = 0, limit: int = 10):
    return db.query(models.Transaction).filter(models.Transaction.account_id == account_id).offset(skip).limit(limit).all()
