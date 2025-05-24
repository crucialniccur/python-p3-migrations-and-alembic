from sqlalchemy import create_engine, desc
from sqlalchemy import (CheckConstraint, UniqueConstraint,
                        Column, DateTime, Integer, String)

from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

engine = create_engine('sqlite:///migrations_test.db')

Base = declarative_base()


class Student(Base):
    __tablename__ = 'students'
    __table_args__ = (
        UniqueConstraint('email', name='unique_email'),
        CheckConstraint('grade BETWEEN 1 and 12',
                        name='grade_between_1_and_12')
    )
