"""
Imports Gspread libray
"""
import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    'https://spreadsheets.google.com/feeds',
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('DailySales')


def get_sales():
    """
    Gets end of day sales
    """
    print("Please enter todays sales as below separated by commas in order")
    print("Food sales, Drink sales, 0% VAT ")
    print("For example: 1234.56, 123, 123.45 \n")

    todays_sales = input("Please Enter Sales here: ")

    sales_data = todays_sales.split(",")
    print(sales_data)
    validate_input(sales_data)


def validate_input(values):
    """
    Convert data to a float.
    raises ValueError if strings cannot be a float
    or if there isnt a value input
    """
    try:
        [float(value) for value in values]
        if len(values) != 3:
            raise ValueError(
                f"3 values seperated by a comma required. Found:{len(values)}"
            )
    except ValueError as e:
        print(f"Invalid Data: {e}, please try again")


get_sales()
