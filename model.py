from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime, timedelta
from sqlalchemy import Column, Integer, Float, Date, String
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import logging
import requests
import sys

Base = declarative_base()
logging.basicConfig(stream=sys.stdout, level=logging.INFO)
API_KEY = "8574ff92a5681a78b1a8c67cc6f14eb4"


class CurrencyData(Base):
    __tablename__ = 'currency_data'
    id = Column(Integer, primary_key=True)
    date = Column(Date, nullable=False)
    currency_country = Column(String(3), nullable=False)
    currency_rate = Column(Float)

    def __repr__(self):
        return f'<currency_data (date={self.date}, currency={self.currency_country}, rate={self.currency_rate}>'


def create_session():
    db = "currency_record.sqlite"
    engine = create_engine(f'sqlite:///{db}')
    Base.metadata.bind = engine
    session = sessionmaker(bind=engine)
    ses = session()
    return ses


if __name__ == '__main__':
    ses = create_session()
    logging.info("One time table creation")
    Base.metadata.create_all()
    today = datetime.now().date()
    for i in range(30, -1, -1):
        day = today - timedelta(i)
        print(i, day)
        logging.info(f"Entering data for day : {day}")
        res = requests.get(
            f'http://data.fixer.io/api/{day}?access_key={API_KEY}&symbols=USD,AUD,CAD,PLN,MXN&format=1').json()
        ses.add_all(
            CurrencyData(date=day, currency_country=currency, currency_rate=value) for currency, value in res['rates'].items()
            )
    ses.commit()
