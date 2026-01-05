import csv

class CurrencyCodeGrabber:

    def __init__(self, file):
        self.currency_dict = self.extract_dict(file)

    def extract_dict(self, file):
        dict = {}

        with open(file, mode="r", newline="", encoding="utf-8") as f:
            reader = csv.reader(f)
            next(reader)
            dict = {
                row[0]: row[1] for row in reader
            }
        
        return dict
    
    def print_table(self):
        for code, name in self.currency_dict.items():
            print(f"{code:<20} {name:<20}")

    def get_name(self, string):
        return self.currency_dict[string]

    def valid_code(self, code):

        if code in self.currency_dict:
            return True
        
        return False
