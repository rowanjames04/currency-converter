import requests
import os

def is_yes_or_no(string):
    return string.lower() == "yes" or string.lower() == "no"

def get_api_key():
    return os.getenv("API_KEY")

def get_url(from_c, to_c):
    return f"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency={from_c}&to_currency={to_c}&apikey={get_api_key()}"

def convert_currency(from_c, to_c, amount):
    url = get_url(from_c, to_c)
    results = requests.get(url).json()
    rate = float(results['Realtime Currency Exchange Rate']['5. Exchange Rate'])
    return amount * rate