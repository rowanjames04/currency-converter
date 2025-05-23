# Currency Converter

[Python 3.x](https://www.python.org/downloads/) | [MIT License](LICENSE)

## Overview

This is a command-line currency converter tool written in Python. It allows users to convert amounts between various physical currencies using real-time exchange rates from the Alpha Vantage API. Currency codes and names are loaded from a local CSV file.

## Features

- Lists available currency codes and names from a CSV file.
- Validates user input for currency codes and amounts.
- Fetches real-time currency exchange rates via the Alpha Vantage API.
- Displays conversion results in a clear format.
- Handles invalid input gracefully.

## Usage Instructions

Run **main.py** to start the currency converter. It will display the list of currency codes and allow you to convert an amount from one currency to another.

If you encounter errors related to invalid currency codes during conversion (for example, if the API returns an error for certain codes), run **validate.py**. This script will:

- Check every currency code in the CSV file against the Alpha Vantage API.
- Identify invalid or unsupported currency codes.
- Remove those invalid entries from the CSV file.
- Save the list of invalid codes to a separate file for review.

**Note:** Because Alpha Vantage enforces a rate limit (typically 5 calls per minute on the free tier), the validation process can take some time (approximately 15 seconds per request). Please be patient while the script runs.

## Setup

1. Make sure you have Python 3 installed.

2. Install the required Python package:

   pip install requests

3. Place the `physical_currency_list.csv` file (containing currency codes and names) in the same folder as the scripts.

4. Obtain a free API key from [Alpha Vantage](https://www.alphavantage.co/support/#api-key) and update the `api_key` variable in both scripts.

## Notes

- The CSV file may become outdated as currencies get added or deprecated over time. Running `validate.py` helps keep it current by removing unsupported codes.
- Always back up your CSV file before running the validation script if you want to keep a record of all original currencies.

## License

This project is licensed under the MIT License.

---

Feel free to open issues or contribute improvements!
