from rich.console import Console
from rich.table import Table
from modules.google_sheets import get_data, new_item_handler, delete_handler, update_handler
from modules.input_validation import user_input
from modules.helpers import is_operation_canceled


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


def search_inventory():
    console = Console()
    data = get_data()

    while True:
        console.print("\n[blue bold underline]Search Inventory")
        options = [
            "[green][bold]1.[/green][/bold] Add",
            "[green][bold]2.[/green][/bold] Update",
            "[green][bold]3.[/green][/bold] Delete",
            "[green][bold]c.[/green][/bold] Cancel",
        ]
        menu = " | ".join(options)
        console.print(menu)

        search_term = user_input("Enter the name of the item to search (or other operation): ")

        # Abort search operation and return to operations menu
        if is_operation_canceled(search_term, "c"):
            return # Exit the function to prevent further execution
        elif search_term == "1":
            add_new_item()
            continue  # Continue the search loop
        elif search_term == "2":
            update_item()
            continue  # Continue the search loop
        elif search_term == "3":
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


def add_new_item():
    console = Console()
    
    console.print("\n[blue bold underline]Add new item")
    console.print("[blue]Fill the fields, or submit 'c' to cancel at any time:\n")
    
    item_name = user_input("Enter item name: ", expected_type="text")
    if is_operation_canceled(item_name, "c"):
        return
    
    item_type = user_input("Enter item type: ", expected_type="text")
    if is_operation_canceled(item_type, "c"):
        return
    
    item_quantity = user_input("Enter item quantity: ", expected_type="positive number")
    if is_operation_canceled(item_quantity, "c"):
        return
    
    item_unit = user_input("Enter item measurement unit: ", expected_type="text")
    if is_operation_canceled(item_unit, "c"):
        return
    
    data = get_data()
    
    item_to_save = [{
        "index": len(data) + 1,
        "name": item_name,
        "type": item_type,
        "quantity": item_quantity,
        "unit": item_unit
    }]
    
    table_title = "Item to save:"
    display_items(item_to_save, table_title)
    
    user_confirmation = user_input("Do you want to save this item? (y/n)", available_options=['y', 'n'])
    if user_confirmation.lower() == 'y':
        item_values = (item_name, item_type, item_quantity, item_unit)
        new_item_handler(item_values)
    elif user_confirmation.lower() == 'n':
        console.print("[yellow]Operation aborted!\n")
        return  # Exit the function after aborting the operation


def delete_item():
    # Prevent circular dependency error 
    from modules.menu import operations_menu
    
    console = Console()
    data = get_data()
    max_index = len(data)

    console.print("\n[blue bold underline]Delete item")
    console.print("[blue]Fill the fields, or submit 'c' to cancel at any time:\n")
    
    while True:
        
        index_to_delete = user_input(f"Enter the index to delete an item (1 - {max_index}): ")

        # Abort deletion and return to operations menu
        if is_operation_canceled(index_to_delete, "c"):
            return # Exit the function to prevent further execution

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

        delete_confirmation = user_input("Are you sure you want to delete this item? (y/n)", ['y', 'n'])
        if delete_confirmation.lower() == 'y':
                # Remove the item from the data list
                delete_handler(index_to_delete)
        else:
            console.print("[yellow]Deletion canceled![/yellow]")
            operations_menu()
            return  # Exit the function after cancellation

        break  # Exit the loop after handling the deletion

    # Refetch data and continue with search loop or other necessary operations
    data = get_data()


def update_item():
    console = Console()
    data = get_data()
    max_index = len(data)

    console.print("\n[blue bold underline]Update item")
    console.print("[blue]Fill the fields, or submit 'c' to cancel at any time:\n")
    
    while True:
        
        index_to_update = user_input(f"Enter the index to update an item (1 - {max_index}): ")
        
        # Abort update and return to operations menu
        if is_operation_canceled(index_to_update, "c"):
            return # Exit the function to prevent further execution

        try:
            index_to_update = int(index_to_update)
            if index_to_update not in range(1, max_index + 1):
                console.print(f"[red]Invalid index '{index_to_update}'. Index should be between 1 and {max_index}.[/red]")
                continue  # Prompt again
        except ValueError:
            console.print(f"[red]Invalid input '{index_to_update}'. Please enter a number.[/red]")
            continue  # Prompt again

        # Display current item
        item_to_update = data[index_to_update - 1]  # Adjust for 0-based indexing
        console.print("\n[bold blue]Item to update:")
        display_items([item_to_update], "")

        console.print("[blue]Fill the fields, or submit 'c' to cancel at any time:\n")
        item_name = user_input(f"Enter new item name (leave blank to keep '{item_to_update['name']}'): ", expected_type="text", allow_empty=True)
        if is_operation_canceled(item_name, "c"):
            return
        item_name = item_name or item_to_update['name']

        item_type = user_input(f"Enter new item type (leave blank to keep '{item_to_update['type']}'): ", expected_type="text", allow_empty=True)
        if is_operation_canceled(item_type, "c"):
            return
        item_type = item_type or item_to_update['type']

        item_quantity = user_input(f"Enter new item quantity (leave blank to keep '{item_to_update['quantity']}'): ", expected_type="positive number", allow_empty=True)
        if is_operation_canceled(item_quantity, "c"):
            return
        item_quantity = item_quantity or item_to_update['quantity']

        item_unit = user_input(f"Enter new item measurement unit (leave blank to keep '{item_to_update['unit']}'): ", expected_type="text", allow_empty=True)
        if is_operation_canceled(item_unit, "c"):
            return
        item_unit = item_unit or item_to_update['unit']

        updated_item = [{
            "index": index_to_update,
            "name": item_name,
            "type": item_type,
            "quantity": item_quantity,
            "unit": item_unit
        }]
        
        table_title = "The new item updated:"
        display_items(updated_item, table_title)
        
        user_confirmation = user_input("Do you want to save this item? (y/n)", available_options=['y', 'n'])
        if user_confirmation.lower() == 'y':
            update_handler(index_to_update, updated_item[0])
        elif user_confirmation.lower() == 'n':
            console.print("[yellow]Operation aborted!\n")
            return  # Exit the function after aborting the operation

        break  # Exit the loop after handling the update

    # Refetch data and continue with search loop or other necessary operations
    data = get_data()
