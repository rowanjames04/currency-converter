from helpers import is_yes_or_no, convert_currency
from client import CurrencyCodeGrabber

def interactive_mode():
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
                amount = float(input("Enter the \033[1mamount\033[0m you wish to convert: "))
                break
            except ValueError:
                print("Try Again! Please Enter a Valid Amount")

        to_c = input(f"Enter the \033[1mCurrency Code\033[0m of the currency you want to convert to: ").upper()
        while not client.valid_code(to_c):
            print("Try Again! Please Enter a Valid Code")
            to_c = input(f"Enter the \033[1mCurrency Code\033[0m of the currency you want to convert to: ").upper()
        
        
        new_amount = convert_currency(
            from_c, 
            to_c, 
            amount
        )

        print(f"{amount} {client.get_name(from_c)} equals {str(new_amount)} {client.get_name(to_c)}")

def args_mode(args):
    client = CurrencyCodeGrabber("physical_currency_list.csv")

    if not client.valid_code(args.from_currency):
        print("Invalid FROM currency code")
        return
    
    if not client.valid_code(args.to_currency):
        print("Invalid TO currency code")
        return
    
    new_amount = convert_currency(
        args.from_currency.upper(),
        args.to_currency.upper(),
        args.amount,
    )
    
    print(f"{args.amount} {args.from_currency.upper()} = {new_amount:.2f} {args.to_currency.upper()}")