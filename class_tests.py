from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import DeclarativeBase
import sqlite3
import pandas as pd

#Base = declarative_base()
class Base(DeclarativeBase):
    pass


class Car(Base):
    __tablename__ = "cars"
    id = Column(Integer, primary_key=True)
    make = Column(String)
    model = Column(String)
    year = Column(Integer)
    specs = Column(String)


api = 'https://data.gov.il/api/3/action/datastore_search'
sql = "sqlite:///cars.db"


engine = create_engine("sqlite:///cars.db")
Base.metadata.create_all(engine)


Session = sessionmaker(bind=engine)
session = Session()


query = session.query(Car).all()
result = [x.year for x in query]
# example list of cars and their specs
cars = [{"make": "Toyota", "model": "Camry", "year": 2020, "specs": "4-cylinder engine"},
        {"make": "Honda", "model": "Civic", "year": 2021, "specs": "6-speed manual transmission"},
        {"make": "Tesla", "model": "Model 3", "year": 2022, "specs": "Long Range Dual Motor"}]


# insert each car into the table
for car in cars:
    session.add(Car(**car))


# save and close the session
session.commit()
session.close()
b=5
