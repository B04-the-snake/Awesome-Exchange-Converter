from os import getenv
from flask import request
import requests as r

# Adding a secret API_V6_KEY from .env
API_KEY = getenv("API_KEY")
AVAILABLE_CURR = ["EUR", "USD", "PLN", "GBP", "AUD", "CHF", "JPY"]


def get_available_curr():
    return AVAILABLE_CURR

def rate_engine():
    # Testowanie
    # print(request.__dir__, "dir")
    # print(request.__dict__, "dict")

    amount = request.args.get('amount')
    amount = float(amount)

    from_curr = request.args.get('from_curr')
    to_curr = request.args.get('to_curr')

    URL = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/{from_curr}"

    response = r.get(url=URL).json()
    rate = response['conversion_rates'][to_curr]
    rate = float(rate)
    result = round(rate * amount, 2)

    return str(result)