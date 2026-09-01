from sqlalchemy import Column, Integer, String
from sqlalchemy import declarative_base

Base = declarative_base()


class BaseClass(Base):
    __tablename__ = "base_table"
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
