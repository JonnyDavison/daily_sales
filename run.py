"""
Imports Gspread libray
"""
import gspread
from google.oauth2.service_account import Credentials
from datetime import date


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
    while True:
        print("Please enter todays sales as below seperated by commas")
        print("Follow the order: Food sales, Drink sales, 0% VAT sales")
        print("For example: 1234.56, 123, 123.45 \n")
        show_date()

        todays_sales = input("Please Enter Sales here: ")

        sales_data = todays_sales.split(",")
    
        if validate_input(sales_data):
            print("Data format is accepted")
            break
    return sales_data    


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
        return False

    return True    


def update_worksheet(data):
    """
    Updates worksheet adding new data
    """
    print("Updating sales sheet... \n")
    sales_worksheet = SHEET.worksheet('sales')
    sales_worksheet.append_row(data)
    print("Update successfull.\n")


def sales_total(value):
    """
    Returns todays total sales to the user & appends to worksheet
    """
    total = sum(value)
    print(f"Total sales: {total} \n")
    sales_worksheet = SHEET.worksheet('sales')
    column = 4
    last_row = len(sales_worksheet.get_all_values())
    sales_worksheet.update_cell(last_row, column, total)


def show_date():
    """
    Returns todays date & appends to worksheet
    """
    today = date.today()
    print(f"Today's date: {today} \n")


def main():
    """
    Calls main progam function 
    """
    data = get_sales()
    sales_values = [float(num) for num in data]
    update_worksheet(sales_values)
    sales_total(sales_values)


print("Welcome to Daily Sales for all your sales reporting needs\n")
main()
