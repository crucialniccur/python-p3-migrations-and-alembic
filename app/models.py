from sqlachemy import create_engine
from sqlachemy.ext.declarative import declarative_base


engine = create_engine('sqliteL//migrations_test.db')

Base = declarative_base()
