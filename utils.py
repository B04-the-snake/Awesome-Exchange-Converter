import requests
from const import URL


def get_available_curr(url=URL):
    return requests.get(url=url + "EUR").json().get("rates").keys()

def validate_form(curr_to_sell, curr_to_buy, amount):
    errors = []
    available_curr = get_available_curr()
    if curr_to_sell not in available_curr:
        errors.append("Not valid currency - curr_to_sell")
    if curr_to_buy not in available_curr:
        errors.append("Not valid currency - curr_to_buy")
    if not amount.isnumeric():
        errors.append("Not valid amount")
    return errors
