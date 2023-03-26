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
    print("Please enter todays sales as below separated by commas")
    print("Food sales, Drink sales, 0% VAT ")
    print("For example: 1234.56, 123.45, 123.45 \n")

    sales = input("Please Enter Sales here: ")
    sales_data = sales.split(",")
    print(sales)
    print(sales_data)
    

get_sales()
