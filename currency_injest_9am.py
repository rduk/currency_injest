from currency_task.model import logging, CurrencyData, API_KEY, Base, create_session
from datetime import datetime
import requests

if __name__ == '__main__':
    ses = create_session()
    Base.metadata.create_all()
    today = datetime.now().date()
    logging.info(f"Entering data for day : {today}")
    res = requests.get(
        f'http://data.fixer.io/api/{today}?access_key={API_KEY}&format=1').json()
    ses.add_all(
        CurrencyData(date=today, currency_country=currency, currency_rate=value) for currency, value in
        res['rates'].items()
    )
    ses.commit()
