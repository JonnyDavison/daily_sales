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
    
        if validate_sales(sales_data):
            print("Sales data format is accepted")
            break
    return sales_data    


def validate_sales(values):
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


def update_sales_sheet(data):
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
    sales_total = sum(value)
    sales_worksheet = SHEET.worksheet('sales')
    column = 4
    last_row = len(sales_worksheet.get_all_values())
    sales_worksheet.update_cell(last_row, column, sales_total)
    return sales_total


def show_date():
    """
    Returns todays date
    """
    today = date.today()
    print(f"Today's date: {today} \n")
    return today


def add_sales_date():
    """
    Adds date to worksheet
    """
    now = str(date.today())
    sales_worksheet = SHEET.worksheet('sales')
    column = 5
    last_row = len(sales_worksheet.get_all_values())
    sales_worksheet.update_cell(last_row, column, now)
    

def get_costs():
    """
    Gets costs for the day incuding Cost of sales(COS) and
    labour costs
    """
    while True:
        print("Please enter todays costs as below seperated by commas")
        print("Follow the order: Food Cost, Labour Cost")
        print("For example: 1234.56, 1234.56 \n")

        todays_costs = input("Please Enter Food Cost then Labour Cost here: ")

        costs_data = todays_costs.split(",")

        if validate_costs(costs_data):
            print("Costs data format is accepted")
            break
    return costs_data


def validate_costs(values):
    """
    Convert data to a float.
    raises ValueError if strings cannot be a float
    or if there isnt a value input
    """
    try:
        [float(value) for value in values]
        if len(values) != 2:
            raise ValueError(
                f"2 values seperated by a comma required. Found:{len(values)}"
            )
    except ValueError as e:
        print(f"Invalid Data: {e}, please try again")
        return False

    return True  


def update_cost_sheet(data):
    """
    Updates worksheet adding new data
    """
    print("Updating costs sheet... \n")
    sales_worksheet = SHEET.worksheet('costs')
    sales_worksheet.append_row(data)
    print("Update successfull.\n")


def cost_total(value):
    """
    Returns todays total sales to the user & appends to worksheet
    """
    cost_total = sum(value)
    costs_worksheet = SHEET.worksheet('costs')
    column = 3
    last_row = len(costs_worksheet.get_all_values())
    costs_worksheet.update_cell(last_row, column, cost_total)
    return cost_total


def add_costs_date():
    """
    Adds date to worksheet
    """
    now = str(date.today())
    cost_worksheet = SHEET.worksheet('costs')
    column = 4
    last_row = len(cost_worksheet.get_all_values())
    cost_worksheet.update_cell(last_row, column, now)


def sales_analysis(num1, num2):
    """
    Creates and returns sales figures to the user and worksheet
    """
    # Prints totals
    print(f"Total Sales :{num1} Total Costs: {num2}")
    # Calulates Gross Margin %
    gross_margin = round(((num2 / num1) * 100), 1)
    print(f"GM% {gross_margin}%")
    # Calulates Cash Margin
    cash_margin = (num1 - num2)
    print(cash_margin)

    return gross_margin
    return cash_margin


def main():
    """
    Calls main progam function 
    """
    # Gets & Update Sales data
    sales = get_sales()
    sales_values = [float(num) for num in sales]
    update_sales_sheet(sales_values)
    sales_total(sales_values)
    add_sales_date()
    # Get & Updates Costs data
    costs = get_costs()
    cost_values = [float(num) for num in costs]
    update_cost_sheet(cost_values)
    cost_total(cost_values)
    add_costs_date()
    # Gets sales & costs totals and provides analysis
    total_sales = sales_total(sales_values)
    total_costs = cost_total(cost_values)
    sales_analysis(total_sales, total_costs)


print("Welcome to Daily Sales for all your sales reporting needs\n")
main()

