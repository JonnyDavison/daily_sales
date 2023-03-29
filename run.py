"""
Imports Gspread libray
"""
from datetime import date
import gspread
from google.oauth2.service_account import Credentials
import pyfiglet


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

        todays_sales = input("Please Enter Sales here: \n")

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
    except ValueError as error:
        print(f"Invalid Data: {error}, please try again")
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


def sales_totals(value):
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

        todays_costs = input("Please Enter Food Cost & Labour Cost here: \n")

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
    except ValueError as error:
        print(f"Invalid Data: {error}, please try again")
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


def cost_totals(value):
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
    Calculate and returns sales figures and returns to user
    """
    # Calulates Gross Margin %
    gross_margin = round((100-((num2 / num1) * 100)), 2)
    print(f"Gross Margin%: {gross_margin}%")
    # Calulates Cash Margin
    cash_margin = num1 - num2
    print(f"Cash Margin {cash_margin} \n")
    # Prints totals
    print(f"Total Sales :{num1} Total Costs: {num2}")
    return [num1, num2, gross_margin, cash_margin]


def labour_analysis():
    """
    Calculates and returns labour % to user and worksheet
    """
    costs_worksheet_total = SHEET.worksheet('costs').col_values(2)
    total_cost = costs_worksheet_total[-1]

    cost_worksheet_labour = SHEET.worksheet('costs').col_values(1)
    labour_result = cost_worksheet_labour[-1]

    labour = round((100-((float(labour_result) / float(total_cost)) * 100)), 2)
    print(f"Labour % : {labour}")
    return labour


def update_results_sheet(data):
    """
    Updates the results worksheet adding new data
    """
    print("Updating results sheet... \n")
    results_worksheet = SHEET.worksheet('results')
    results_worksheet.append_row(data)
    print("Update successfull.\n")


def main():
    """
    Calls main progam function
    """
    # Gets & Update Sales data
    sales = get_sales()
    sales_values = [float(num) for num in sales]
    update_sales_sheet(sales_values)
    sales_totals(sales_values)
    add_sales_date()
    # Get & Updates Costs data
    costs = get_costs()
    cost_values = [float(num) for num in costs]
    update_cost_sheet(cost_values)
    cost_totals(cost_values)
    add_costs_date()
    # Gets sales & costs totals and provides analysis
    total_sales = sales_totals(sales_values)
    total_costs = cost_totals(cost_values)
    labour_cost = labour_analysis()
    analysis = sales_analysis(total_sales, total_costs) + [labour_cost]
    update_results_sheet(analysis)


logo = pyfiglet.figlet_format("Daily   Sales")
print(logo)
print("Welcome to Daily Sales for all your sales reporting needs\n")
print("Aiming to provide you with all your financial reporting needs")
end = pyfiglet.figlet_format("Thank   you \n for   using \nDailySales")
print(end)
