# backend/models/transactions.py

from sqlalchemy import Column, Integer, String
from .database import Base

class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True)
    group_id = Column(Integer)
    payer = Column(String)
    participants = Column(String)  # CSV string: "A,B,C"
    total_amount = Column(Integer)
    split_type = Column(String)    # equal / ratio
    details = Column(String)       # extra JSON-like notes
    category = Column(String)      # e.g. travel, food, groceries, etc.
