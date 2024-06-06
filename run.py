import gspread
from google.oauth2.service_account import Credentials
from rich.console import Console
from rich.prompt import Prompt
from rich.table import Table
import sys
import os


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
    inventory_sheet = SHEET.worksheet('inventory_sheet')
    inventory_data = inventory_sheet.get_all_values()
    data = convert_to_dict(inventory_data)
    return data

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
    for i, row in enumerate(data[1:], start=1): # Start from 1 to match Google Sheets row numbers
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
    
def main_menu():
    console = Console()
    console.print("\n[blue bold underline]Inventory Management System")
    
    options = [
        "[green][bold]1.[/green][/bold] View Inventory",
        "[green][bold]2.[/green][/bold] Operations",
        "[green][bold]0.[/green][/bold] Exit"
    ]
    
    menu = " | ".join(options)
    console.print(menu)
    
    choices = ["1", "2", "0"]
    input = user_input("Choose an operation: ", choices, True)
    
    return input


def operations_menu():
    console = Console()
    while True:
        console.print("\n[blue bold underline]Operation selector")
        options = [
            "[green][bold]1.[/green][/bold] Add",
            "[green][bold]2.[/green][/bold] Update",
            "[green][bold]3.[/green][/bold] Delete",
            "[green][bold]4.[/green][/bold] Search",
            "[green][bold]0.[/green][/bold] Back",
        ]
        menu = " | ".join(options)
        console.print(menu)

        choices = ["1", "2", "3", "4", "0"]
        input = user_input("Choose an operation: ", choices, True)

        if input == "1":
            print("Add functionality not implemented yet...")
        elif input == "2":
            print("Update not implemented yet...")
        elif input == "3":
            delete_item()
        elif input == "4":
            search_inventory()
        elif input == "0":
            return  # Return to the previous menu
    

def user_input(label, available_options, strict_input):
    console = Console()
    user_prompt = input(label).strip()
    
    if strict_input:
        if user_prompt not in available_options:
            console.print("[bold red]Please select one of the available options\n")
            user_prompt = input(label)
        else:
            return user_prompt
    else:
        return user_prompt


def search_inventory():
    console = Console()
    data = get_data()

    while True:
        console.print("\n[blue bold underline]Search Inventory")
        options = [
            "[green][bold]1.[/green][/bold] Update",
            "[green][bold]2.[/green][/bold] Delete",
            "[green][bold]0.[/green][/bold] Back",
        ]
        menu = " | ".join(options)
        console.print(menu)

        search_term = user_input("Enter the name of the item to search (or other operation): ", "", False)

        if search_term == "0":
            print("Going back...")
            return  # Return to the operations menu
        elif search_term == "1":
            print("Update not implemented yet...")
            continue  # Continue the search loop
        elif search_term == "2":
            delete_item()
            continue  # Continue the search loop

        found_items = [item for item in data if search_term.lower() in item["name"].lower()]
        filtered_data = []
        if found_items:
            # Render results and continue search loop
            for item in found_items:
                filtered_data.append(item)
            table_title = f"Search results for {search_term}" if search_term else "Inventory Items"
            display_items(filtered_data, table_title)
        else:
            console.print(f"\n[red]No items or operation found for [bold]'{search_term}'[/bold].\n")


def delete_item():
    console = Console()
    data = get_data()
    max_index = len(data)

    while True:
        index_to_delete = user_input(f"Enter the index to delete an item (1 - {max_index}), or '0' to cancel: ", "", False)

        # Abort deletion and return to operations menu
        if index_to_delete == '0':
            operations_menu()
            return  # Exit the function to prevent further execution

        try:
            index_to_delete = int(index_to_delete)
            if index_to_delete not in range(1, max_index + 1):
                console.print(f"[red]Invalid index '{index_to_delete}'. Index should be between 1 and {max_index}.[/red]")
                continue  # Prompt again
        except ValueError:
            console.print(f"[red]Invalid input '{index_to_delete}'. Please enter a number.[/red]")
            continue  # Prompt again

        # Delete
        item_to_delete = data[index_to_delete - 1]  # Adjust for 0-based indexing

        console.print("\n[bold red]Item to delete:")
        display_items([item_to_delete], "")

        delete_confirmation = user_input("Are you sure you want to delete this item? (y/n)", ['y', 'n'], True)
        if delete_confirmation.lower() == 'y':
            try:
                # Remove the item from the data list
                inventory_sheet = SHEET.worksheet('inventory_sheet')
                inventory_sheet.delete_rows(index_to_delete + 1)

                console.print("[green]Item deleted successfully![/green]\n")
            except Exception as e:
                console.print(f"[bold red]Error deleting item: {str(e)}[/bold red]\n")
        else:
            console.print("[yellow]Deletion canceled![/yellow]")
            operations_menu()
            return  # Exit the function after cancellation

        break  # Exit the loop after handling the deletion

    # Refetch data and continue with search loop or other necessary operations
    data = get_data()

        

def main():
    """Run all program functions
    """
    os.system("clear")
    
    start_view()
    
    while True:
        choice = main_menu()
        if choice == "1":
            data = get_data()
            display_items(data, "Inventory Items")
        elif choice == "2":
            operations_menu()
        elif choice == "0":
            print("Quitting the application...")
            sys.exit()
    

main()
    
