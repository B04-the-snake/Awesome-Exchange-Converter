import requests
from const import URL

def exchange_engine(curr_to_sell, curr_to_buy, amount, url=URL):
	r = requests.get(url=url + curr_to_sell)
	currencies = r.json().get("rates")
	# there we should use this function from  utils to get currencies
	while curr_to_sell not in currencies or curr_to_buy not in currencies:
		raise Exception("\nNie ma takiej waluty! Podaj poprawną walutę.")
		curr_to_sell = input("\nJaką walutę chcesz sprzedać ? ")
		curr_to_buy = input("Jaką walutę chcesz kupić ? ")

	while not amount.replace(".", "", 1).isdigit():
		amount = input("Podaj wartość liczbową! \nPodaj ilość: ")
	amount = float(amount)


	return currencies[curr_to_buy] * amount
