# Anna Liner
# Python Unit Testing Challenge

import unittest
from datetime import datetime

# recreate a mock version of the get_input function from request.py that validates formats, but does not make chart 
def get_valid_input(stock_symbol, chart_type, time_series, start_date, end_date):

    # check stock symbol
    if not (stock_symbol.isupper() and stock_symbol.isalpha() and 1 <= len(stock_symbol) <= 7):
        print("\nThe stock symbol is incorrectly entered. It must be uppercase, and 1-7 alphabetic characters!")
        return False

    # check chart type
    if not (chart_type.isdigit() and (chart_type == "1" or chart_type == "2")):
        print("\nThe chart type is incorrectly entered. It must be the digit 1 or 2 only.")
        return False
        
    # check time series
    if not (time_series.isdigit() and 1 <= int(time_series) <= 4):
        print("\nThe time series is incorrectly entered. It must be a digit from 1 through 4 only.")
        return False

    # convert start and end date as YYYY-MM-DD (https://www.geeksforgeeks.org/python-datetime-strptime-function/)
    try: 
        datetime.strptime(start_date, "%Y-%m-%d")
        datetime.strptime(end_date, "%Y-%m-%d")
    except ValueError:
        print("\nIncorrect data format, should be YYYY-MM-DD")
        return False

    return True

# test multipe inputs using unittest TestCase
class TestGetInput(unittest.TestCase):

    # 1. runs a test to check valid input
    def test_valid_inputs(self):
        self.assertTrue(get_valid_input("GOOGL", "2", "3", "2019-03-03", "2020-04-10"))

    # 2. runs a test to check for invalid input for the stock symbol
    def test_valid_symbol(self):
        self.assertFalse(get_valid_input("1234567@", "2", "3", "2019-03-03", "2020-04-10"))

    # 3. runs a test to check for invalid chart type input
    def test_valid_chart(self):
        self.assertFalse(get_valid_input("GOOGL", "3", "3", "2019-03-03", "2020-04-10"))

    # 4. runs a test to check for invalid time series input
    def test_valid_time_series(self):
        self.assertFalse(get_valid_input("GOOGL", "2", "6", "2019-03-03", "2020-04-10"))

    # 5. runs a test to check for invalid start date input
    def test_valid_start_date(self):
        self.assertFalse(get_valid_input("GOOGL", "2", "3", "19-03-03", "2020-04-10"))

    # 6. runs a test to check for invalid end date input
    def test_valid_end_date(self):
        self.assertFalse(get_valid_input("GOOGL", "2", "3", "2019-03-03", "10-04-2020"))
    
# lets you run without long command
if __name__ == "__main__":
    unittest.main()