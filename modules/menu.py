from rich.console import Console
from modules.input_validation import user_input
from modules.inventory_management import (
    add_new_item,
    update_item,
    delete_item,
    search_inventory,
    display_help
)


def main_menu():
    console = Console()
    console.print("\n[blue bold underline]Inventory Management System")

    options = [
        "[green][bold]1.[/green][/bold] View Inventory",
        "[green][bold]2.[/green][/bold] Operations",
        "[green][bold]9.[/green][/bold] Help",
        "[green][bold]0.[/green][/bold] Exit"
    ]

    menu = " | ".join(options)
    console.print(menu)

    choices = ["1", "2", "9", "0"]
    input = user_input("Choose an operation: ", choices)

    return input


def operations_menu():
    console = Console()

    while True:
        console.print("\n[blue bold underline]Operations Menu")
        options = [
            "[green][bold]1.[/green][/bold] Add",
            "[green][bold]2.[/green][/bold] Update",
            "[green][bold]3.[/green][/bold] Delete",
            "[green][bold]4.[/green][/bold] Search",
            "[green][bold]9.[/green][/bold] Help",
            "[green][bold]0.[/green][/bold] Back",
        ]
        menu = " | ".join(options)
        console.print(menu)

        available_options = ["1", "2", "3", "4", "9", "0"]
        selection = user_input("Select an option: ", available_options)

        if selection == '0':
            break  # Exit the loop and end the program
        elif selection == '1':
            add_new_item()
        elif selection == '2':
            update_item()
        elif selection == '3':
            delete_item()
        elif selection == '4':
            search_inventory()
        elif selection == '9':
            display_help()
