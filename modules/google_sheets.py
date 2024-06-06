import gspread
from google.oauth2.service_account import Credentials
from rich.console import Console
from modules.helpers import convert_to_dict


# Connect to Google Sheets API
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('Inventory')


def get_data():
    console = Console()
    try:
        inventory_sheet = SHEET.worksheet('inventory_sheet')
        inventory_data = inventory_sheet.get_all_values()
        data = convert_to_dict(inventory_data)
        return data
    except Exception as e:
        console.print(f"[bold red]Failed to retrieve Inventory data: {str(e)}\n")

