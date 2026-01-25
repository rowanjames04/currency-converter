import argparse

def parse_args():
    parser = argparse.ArgumentParser(description="Currency Converter")

    parser.add_argument(
        "--from", 
        dest="from_currency", 
        help="Currency to convert from"
    )
    
    parser.add_argument(
        "--to", 
        dest="to_currency", 
        help="Currency to convert to"
    )

    parser.add_argument(
        "--amount", 
        type=float, 
        help="Amount to convert"
    )

    return parser.parse_args()
