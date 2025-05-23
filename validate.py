# validate.py
import requests
import csv
import os
import time

api_key = 'I1LQZODF7N8OEVPG'
base_currency = 'USD'
delay_seconds = 15  # For Alpha Vantage free API rate limit

pyfile_dir = os.path.dirname(os.path.abspath(__file__))
csv_file = os.path.join(pyfile_dir, 'physical_currency_list.csv')
invalid_file = os.path.join(pyfile_dir, 'invalid_currency_codes.txt')

valid_rows = []
invalid_codes = []

# Read CSV and validate each currency code
with open(csv_file, mode='r', newline='') as file:
    reader = csv.reader(file)
    header = next(reader)
    for row in reader:
        code = row[0].strip().upper()
        if code == base_currency:
            valid_rows.append(row)
            continue

        url = f"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency={base_currency}&to_currency={code}&apikey={api_key}"
        response = requests.get(url)
        data = response.json()

        if "Error Message" in data:
            print(f"Invalid code: {code}")
            invalid_codes.append(code)
        else:
            print(f"Valid code: {code}")
            valid_rows.append(row)

        time.sleep(delay_seconds)

# Write invalid codes to file
with open(invalid_file, 'w') as f:
    for code in invalid_codes:
        f.write(code + '\n')

# Overwrite original CSV with only valid rows
with open(csv_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(header)
    writer.writerows(valid_rows)

print("\nValidation complete.")
print(f"Invalid codes saved to: {invalid_file}")
print(f"{len(invalid_codes)} invalid entries removed from {csv_file}.")
