from os import getenv
from flask import request
import requests as r

# Adding a secret API_V6_KEY from .env
API_KEY = getenv("API_KEY")
AVAILABLE_CURR = ["EUR", "USD", "PLN", "GBP", "AUD", "CHF", "JPY"]


def get_available_curr():
    return AVAILABLE_CURR

def rate_engine(amount,from_curr,to_curr):
    # Testowanie
    # print(request.__dir__, "dir")
    # print(request.__dict__, "dict")
    URL = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/{from_curr}"
    try:
        response = r.get(url=URL).json()
        rate = float(response['conversion_rates'][to_curr])
    # no bare except
    except:
        return "coś poszło nie tak"
    return str(round(rate * amount, 2))