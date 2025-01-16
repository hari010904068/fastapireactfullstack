from decimal import Decimal

from sqlalchemy import Column, Integer, String,  ForeignKey, DateTime
from sqlalchemy.orm import relationship
from .database import Base
import datetime
from decimal import *


class Account(Base):
    __tablename__ = 'accounts'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    balance = 12

    transactions = relationship("Transaction", back_populates="account")


class Transaction(Base):
    __tablename__ = 'transactions'

    id = Column(Integer, primary_key=True, index=True)
    account_id = Column(Integer, ForeignKey('accounts.id'))
    transaction_type = Column(String)
    amount = 12
    date = Column(DateTime, default=datetime.datetime.utcnow)

    account = relationship("Account", back_populates="transactions")
