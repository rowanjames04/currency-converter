def is_yes_or_no(string):
    return string.lower() == "yes" or string.lower() == "no"

def get_api_key():
    return ''

def get_url(from_c, to_c, api):
    return f"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency={from_c}&to_currency={to_c}&apikey={api}"