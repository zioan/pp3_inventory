from rich.console import Console
from rich.table import Table
from modules.input_validation import user_input
from modules.google_sheets import (
    get_data,
    new_item_handler,
    delete_handler,
    update_handler
)
from modules.helpers import (
    is_operation_canceled,
    get_valid_index,
    get_updated_value
)


def display_items(data, table_title):
    """Display inventory items in a formatted table using the Rich library.

    Args:
        data (list): A list of dictionaries, each dictionary represents
                an inventory item with keys 'name', 'type', 'quantity', 'unit'.
    Returns: None
    """
    console = Console()

    # If no items in inventory, display a message and prevent further execution
    if not data:
        console.print("[bold red]No items in inventory.[/bold red]")
        return

    # Create a table
    print("\n")
    table = Table(title=table_title)

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
        table.add_section()  # Add a horizontal line after each row

    # Print the table to the console
    console.print(table, "\n")


def search_inventory():
    console = Console()

    while True:
        console.print("\n[blue bold underline]Search Inventory")
        options = [
            "[green][bold]1.[/green][/bold] Add",
            "[green][bold]2.[/green][/bold] Update",
            "[green][bold]3.[/green][/bold] Delete",
            "[green][bold]9.[/green][/bold] Help",
            "[green][bold]c.[/green][/bold] Cancel",
        ]
        menu = " | ".join(options)
        console.print(menu)

        query = user_input("Search by name (or choose an operation): ")

        # Abort search operation and return to operations menu
        if is_operation_canceled(query, "c"):
            return  # Exit the function to prevent further execution
        elif query == "1":
            add_new_item()
            continue  # Continue the search loop
        elif query == "2":
            update_item()
            continue
        elif query == "3":
            delete_item()
            continue
        elif query == "9":
            display_help()
            continue

        data = get_data()
        results = [
            item
            for item in data
            if query.lower() in item["name"].lower()
        ]

        filtered_data = []
        if results:
            # Render results and continue search loop
            for item in results:
                filtered_data.append(item)
            table_title = f'Search results for "{query}"'
            display_items(filtered_data, table_title)
        else:
            console.print(f"\n[red]No items found for [bold]'{query}'.\n")


def add_new_item():
    console = Console()

    console.print("\n[blue bold underline]Add new item")
    console.print("[blue]Enter details or 'c' to cancel:[/blue]\n")

    item_name = user_input("Enter item name: ", type="text")
    if is_operation_canceled(item_name, "c"):
        return

    item_type = user_input("Enter item type: ", type="text")
    if is_operation_canceled(item_type, "c"):
        return

    item_quantity = user_input("Enter item quantity: ", type="positive number")
    if is_operation_canceled(item_quantity, "c"):
        return

    item_unit = user_input("Enter item measurement unit: ", type="text")
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

    conf_message = "Do you want to save this item? (y/n)"
    user_conf = user_input(conf_message, available_options=['y', 'n'])
    if user_conf.lower() == 'y':
        item_values = (item_name, item_type, item_quantity, item_unit)
        new_item_handler(item_values)
    elif user_conf.lower() == 'n':
        console.print("[yellow]Operation aborted!\n")
        return  # Exit the function after aborting the operation


def delete_item():

    console = Console()
    data = get_data()

    console.print("\n[blue bold underline]Delete item")
    console.print("[blue]Enter details or 'c' to cancel:[/blue]\n")

    while True:
        item_index = get_valid_index(data, "Enter the index to delete an item")
        if item_index is None:
            return

        # Delete
        item_to_delete = data[item_index - 1]  # Adjust for 0-based indexing

        console.print("\n[bold red]You are about to delete this item:")
        display_items([item_to_delete], "")

        delete_message = "Are you sure you want to delete this item? (y/n)"
        available_options = ['y', 'n']
        delete_confirmation = user_input(delete_message, available_options)
        if delete_confirmation.lower() == 'y':
            # Remove the item from the data list
            delete_handler(item_index)
            break  # Exit the loop after handling the deletion
        else:
            console.print("[yellow]Deletion canceled!\n")
            return  # Exit the function after cancellation


def update_item():
    console = Console()
    data = get_data()

    console.print("\n[blue bold underline]Update item")
    console.print("[blue]Enter details or 'c' to cancel:[/blue]\n")

    while True:

        index_to_update = get_valid_index(data, "Enter item index to update:")
        if index_to_update is None:
            return

        # Display current item
        item_to_update = data[index_to_update - 1]  # Adjust for 0-based index
        console.print("\n[bold blue]Item to update:")
        display_items([item_to_update], "")

        console.print("[blue]Enter details or 'c' to cancel:[/blue]\n")

        item_name = get_updated_value(item_to_update, "name", "text")
        # If user cancels the operation while entering a value
        if item_name is None:
            return

        item_type = get_updated_value(item_to_update, "type", "text")
        if item_type is None:
            return

        item_quantity = get_updated_value(
            item_to_update,
            "quantity",
            "positive number"
        )
        if item_quantity is None:
            return

        item_unit = get_updated_value(item_to_update, "unit", "text")
        if item_unit is None:
            return

        updated_item = [{
            "index": index_to_update,
            "name": item_name,
            "type": item_type,
            "quantity": item_quantity,
            "unit": item_unit
        }]

        table_title = "The new item updated:"
        display_items(updated_item, table_title)

        confirmation_message = "Do you want to save this item? (y/n)"
        available_options = ['y', 'n']
        user_confirmation = user_input(confirmation_message, available_options)
        if user_confirmation.lower() == 'y':
            update_handler(index_to_update, updated_item[0])
        elif user_confirmation.lower() == 'n':
            console.print("[yellow]Operation aborted!\n")
            return  # Exit the function after aborting the operation

        break  # Exit the loop after handling the update

    # Refetch data and continue with search loop or other necessary operations
    data = get_data()


def display_help():
    console = Console()

    help_text = """
    [blue bold underline]Inventory Management Help[/blue bold underline]
    
    [bold underline]Main Menu Options:[/bold underline]
    [bold]1. View Inventory:[/bold]
      - Displays the current inventory items.
    [bold]2. Operations:[/bold]
      - Navigate to the operations menu to manage inventory items.
    [bold]9. Help:[/bold]
      - Displays this help section.
    [bold]0. Exit:[/bold]
      - Exit the application.

    [bold underline]Operations Menu Options:[/bold underline]
    [bold]1. Add:[/bold]
      - Select this option to add a new item to the inventory.
      - You will be prompted to enter the item's details.
      - You can cancel the operation at any time by entering 'c'.
    [bold]2. Update:[/bold]
      - Select this option to update an existing item in the inventory.
      - You will be prompted to enter the index of the item you wish to update.
      - You will get a prompt for each detail (name, type, quantity and unit).
      - You can leave the prompt empty to keep the previous value.
      - You can cancel the operation at any time by entering 'c'.
    [bold]3. Delete:[/bold]
      - Select this option to delete an item from the inventory.
      - You will be prompted to enter the index of the item you wish to delete.
      - You will be asked to confirm the deletion.
      - You can cancel the operation at any time by entering 'c'.
    [bold]4. Search:[/bold]
      - Select this option to search for items in the inventory.
      - This operation will run until you choose to return to the main menu.
      - You can search by entering the name of the item.
      - You can also select one of the other operations (Add, Update, Delete).
      - You can cancel the operation at any time by entering 'c'.
    [bold]9. Help:[/bold]
      - Displays this help section.
    [bold]0. Back:[/bold]
      - Returns to the previous menu or exits the application.

    [bold underline]General Instructions:[/bold underline]
    - Ensure that your inputs do not exceed 20 characters.
    - Follow the prompts carefully and enter the required information.
    - Use 'c' to cancel any operation and return to the main menu.
    - For better clarity on which item to edit or delete,
      I recommend using these functions in conjunction with the search feature.
    """

    console.print(help_text)
