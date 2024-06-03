import gspread
from google.oauth2.service_account import Credentials
from rich.console import Console
from rich.prompt import Prompt
from rich.table import Table

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


def display_items(data):
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
  

def main():
    """Run all program functions
    """
    inventory_sheet = SHEET.worksheet('inventory_sheet')
    inventory_data = inventory_sheet.get_all_values()
    data = convert_to_dict(inventory_data)
    
    start_view()
    display_items(data)

main()
    
