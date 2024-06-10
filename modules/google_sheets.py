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


def new_item_handler(new_item):
    console = Console()
    try:
        inventory_sheet = SHEET.worksheet('inventory_sheet')
        inventory_sheet.append_row(new_item)
        console.print("[green]Item saved successfully!\n")
    except Exception as e:
        console.print(f"[bold red]Failed to save item: {str(e)}\n")


def delete_handler(index):
    console = Console()
    try:
        inventory_sheet = SHEET.worksheet('inventory_sheet')
        inventory_sheet.delete_rows(index + 1)  # Google Sheets is 1-based index
        console.print("[green]Item deleted successfully![/green]\n")
    except Exception as e:
        console.print(f"[bold red]Error deleting item: {str(e)}[/bold red]\n")


def update_handler(index_to_update, item):
    console = Console()
    try:
        # Update the item in the Google Sheet
        inventory_sheet = SHEET.worksheet('inventory_sheet')
        inventory_sheet.update_cell(index_to_update + 1, 1, item["name"])  # Update item name
        inventory_sheet.update_cell(index_to_update + 1, 2, item["type"])  # Update item type
        inventory_sheet.update_cell(index_to_update + 1, 3, item["quantity"])  # Update item quantity
        inventory_sheet.update_cell(index_to_update + 1, 4, item["unit"])  # Update item unit

        console.print("[green]Item updated successfully![/green]\n")
    except Exception as e:
        console.print(f"[bold red]Error updating item: {str(e)}[/bold red]\n")