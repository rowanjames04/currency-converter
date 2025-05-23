import requests
import csv
import os

pyfile_dir = os.path.dirname(os.path.abspath(__file__))

api_key = 'I1LQZODF7N8OEVPG'
file = os.path.join(pyfile_dir, 'physical_currency_list.csv')

def ccstate(code):
    return len(code) and code in validcodes

def isyesno(s):
    return s.lower() == "yes" or s.lower() == "no"

def returncurrencyname(data, code):
    for row in data:
        if row[0].strip().upper() == code.strip().upper():
            return row[1].strip()
    return "Currency Not Found"


while True:

    startend = input("Do you wish to continue? (Yes/No): ")
    while not isyesno(startend):
        print("Try Again! Please Enter a Valid Input")
        startend = input("Do you wish to continue? (Yes/No): ")
    if startend.lower() == "no":
        break

    print(os.getcwd())
    print("-----------------------------------------------------")
    print()

    validcodes = []
    currencydata = []

    with open(file, mode='r') as file:
        reader = csv.reader(file)
        header = next(reader)
        print(f"{header[0]:<20} {header[1]:<20}")
        print("-" * 40)
        
        for row in reader:
            validcodes.append(row[0])
            currencydata.append(row)
            print(f"{row[0]:<20} {row[1]:<20}")

    print()
    print("-----------------------------------------------------")
    print()

    from_c = input(f"Enter the \033[1mCurrency Code\033[0m of the currency you want to convert from: ").upper()
    while not ccstate(from_c):
        print("Try Again! Please Enter a Valid Code")
        from_c = input(f"Enter the \033[1mCurrency Code\033[0m of the currency you want to convert from: ").upper()

    while True:
        try:
            amount_from = float(input("Enter the \033[1mamount\033[0m you wish to convert: "))
            break
        except ValueError:
            print("Try Again! Please Enter a Valid Amount")


    to_c = input(f"Enter the \033[1mCurrency Code\033[0m of the currency you want to convert to: ").upper()
    while not ccstate(to_c):
        print("Try Again! Please Enter a Valid Code")
        to_c = input(f"Enter the \033[1mCurrency Code\033[0m of the currency you want to convert to: ").upper()

    url = f"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency={from_c}&to_currency={to_c}&apikey={api_key}"

    results = requests.get(url).json()
    rate = float(results['Realtime Currency Exchange Rate']['5. Exchange Rate'])

    print(f"{amount_from} {returncurrencyname(currencydata, from_c)} equals {str(amount_from * rate)} {returncurrencyname(currencydata, to_c)}")

