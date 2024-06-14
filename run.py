import sys
import os
from rich.console import Console
from art import text2art
from modules.menu import main_menu, operations_menu
from modules.inventory_management import display_items, display_help
from modules.google_sheets import get_data


def start_view():
    """Display the welcome message with ASCII art."""
    console = Console()
    ascii_art = text2art("Inventory")
    console.print(f"[green bold]{ascii_art}[/green bold]")


def main():
    """Run the main program loop."""
    os.system("clear")

    start_view()

    while True:
        choice = main_menu()
        if choice == "1":
            data = get_data()
            display_items(data, "Inventory Items")
        elif choice == "2":
            operations_menu()
        elif choice == '9':
            display_help()
        elif choice == "0":
            print("Quitting the application...")
            sys.exit()


# Run the main function only if this script is executed directly
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        # Handle the keyboard interrupt exception when the user presses Ctrl+C
        print("\nApplication terminated by user. Quitting the application...")
        sys.exit(0)
