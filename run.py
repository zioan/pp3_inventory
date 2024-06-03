import gspread
from google.oauth2.service_account import Credentials
from rich.console import Console
from rich.prompt import Prompt
from rich.table import Table
import sys


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


def convert_to_dict(data):
    """Convert data from Google Sheets API into a list of dictionaries.
    
    Args:
        data (list): A list of lists where the first sublist contains headers 
                     and subsequent sublists contain inventory data.
                     
    Returns:
        list: A list of dictionaries representing the inventory data.
    """
    # Extract the headers from the first row
    headers = data[0]
    # Initialize an empty list to store the dictionaries
    result = []
    # Iterate over each row in the data starting from the second row
    for i, row in enumerate(data[1:], start=2): # Start from 2 to match Google Sheets row numbers
        # Create a dictionary for the current row
        row_dict = {
            "index": i, # Use the loop index as the row number. "index", number
            headers[0].lower(): row[0],  # "name"
            headers[1].lower(): row[1],  # "type"
            headers[2].lower(): row[2],  # "quantity", string
            headers[3].lower(): row[3]   # "unit"
        }
        # Add the dictionary to the result list
        result.append(row_dict)
    return result 


def display_items(data, table_title):
    """Display inventory items in a formatted table using the Rich library.
    
    Args:
        data (list): A list of dictionaries, where each dictionary represents 
                     an inventory item with keys 'name', 'type', 'quantity', and 'unit'.
                     
    Returns: None
    """
    console = Console()
    
    # If no items in inventory, display a message and prevent further execution
    if not data:
        console.print("[bold red]No items in inventory.[/bold red]")
        return

    # Create a table
    print("\n")
    table = Table(title = table_title)

    # Add columns to the table with styles
    table.add_column("Index", style="yellow")
    table.add_column("Name", style="yellow")
    table.add_column("Type", style="yellow")
    table.add_column("Quantity", justify="right", style="yellow")
    table.add_column("Unit", style="yellow")

    # Iterate over each item in the data list
    for item in data:
        # Add a row to the table for each item
        table.add_row(
            str(item["index"]),
            item["name"],
            item["type"],
            item["quantity"],
            item["unit"]
        )
        table.add_section() # Add a horizontal line after each row

     # Print the table to the console
    console.print(table, "\n")


def start_view():
    console = Console()
    ascii_art = """
'||'                                      .                            
 ||  .. ...   .... ...   ....  .. ...   .||.    ...   ... ..  .... ... 
 ||   ||  ||   '|.  |  .|...||  ||  ||   ||   .|  '|.  ||' ''  '|.  |  
 ||   ||  ||    '|.|   ||       ||  ||   ||   ||   ||  ||       '|.|   
.||. .||. ||.    '|     '|...' .||. ||.  '|.'  '|..|' .||.       '|    
                                                              .. |     
                                                               ''
"""

    console.print(f"[green]{ascii_art}[/green]")
    
def display_menu():
    console = Console()
    console.print("[blue bold underline]Inventory Management System")
    console.print("[green][bold]1.[/green][/bold] View Entire Inventory")
    console.print("[green][bold]2.[/green][/bold] Search Inventory")
    # console.print("[green][bold]3.[/green][/bold] Edit Item")
    # print("4. Update Item")
    # print("5. Delete Item")
    # print("6. Help")
    console.print("[green][bold]7.[/green][/bold] Exit Inventory")
    choice = input("Enter your choice: ")
    return choice


def search_inventory(data):
    console = Console()
    
    search_term = input("Enter the name of the item to search (or '0' to return to menu): ").strip()
    
    if search_term == "0":
        return  # Return to the main menu
    
    found_items = [item for item in data if search_term.lower() in item["name"].lower()]
    filtered_data = []
    if found_items:
        for item in found_items:
            filtered_data.append(item)
        display_items(filtered_data, f"Search results for {search_term}")
        search_inventory(data) # Keep search active until user return to main menu
    else:
        console.print(f"\n[red]No items found for [bold]'{search_term}'[/bold].\n")
        search_inventory(data)
        
  

def main():
    """Run all program functions
    """
    inventory_sheet = SHEET.worksheet('inventory_sheet')
    inventory_data = inventory_sheet.get_all_values()
    data = convert_to_dict(inventory_data)
    console = Console()
    
    start_view()
    
    while True:
        choice = display_menu()
        if choice == "1":
            display_items(data, "Inventory Items")
        elif choice == "2":
            search_inventory(data)
        # elif choice == "3":
        #     edit_item(inventory)
        # elif choice == "4":
        #     update_item(data)
        # elif choice == "5":
        #     delete_item(inventory)
        # elif choice == "6":
        #     display_help()
        elif choice == "7":
            print("Quitting the application...")
            sys.exit()
        else:
            console.print("\n[red]Invalid operation. Please select again.\n")
    
    display_menu()
    # display_items(data)

main()
    
