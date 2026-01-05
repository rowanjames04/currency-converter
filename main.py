import requests

from core import is_yes_or_no, get_api_key, get_url
from csv_reader import CurrencyCodeGrabber

def main():
    while True:
        startend = input("Do you wish to continue? (Yes/No): ")
        while not is_yes_or_no(startend):
            print("Try Again! Please Enter a Valid Input")
            startend = input("Do you wish to continue? (Yes/No): ")
        if startend.lower() == "no":
            break

        print("-----------------------------------------------------")
        print()

        client = CurrencyCodeGrabber("physical_currency_list.csv")
        client.print_table()

        print()
        print("-----------------------------------------------------")
        print()

        from_c = input(f"Enter the \033[1mCurrency Code\033[0m of the currency you want to convert from: ").upper()
        while not client.valid_code(from_c):
            print("Try Again! Please Enter a Valid Code")
            from_c = input(f"Enter the \033[1mCurrency Code\033[0m of the currency you want to convert from: ").upper()

        while True:
            try:
                amount_from = float(input("Enter the \033[1mamount\033[0m you wish to convert: "))
                break
            except ValueError:
                print("Try Again! Please Enter a Valid Amount")

        to_c = input(f"Enter the \033[1mCurrency Code\033[0m of the currency you want to convert to: ").upper()
        while not client.valid_code(to_c):
            print("Try Again! Please Enter a Valid Code")
            to_c = input(f"Enter the \033[1mCurrency Code\033[0m of the currency you want to convert to: ").upper()
        
        url = get_url(from_c, to_c, get_api_key())

        results = requests.get(url).json()
        rate = float(results['Realtime Currency Exchange Rate']['5. Exchange Rate'])

        print(f"{amount_from} {client.get_name(from_c)} equals {str(amount_from * rate)} {client.get_name(to_c)}")


main()