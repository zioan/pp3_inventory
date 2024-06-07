import sys
import os
from rich.console import Console
from art import text2art
from modules.menu import main_menu, operations_menu
from modules.inventory_management import display_items
from modules.google_sheets import get_data


def start_view():
    console = Console()
    ascii_art = text2art("Inventory")
    console.print(f"[green bold]{ascii_art}[/green bold]")

       

def main():
    """Run all program functions"""
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
    

# Run the main function only if this script is executed directly
if __name__ == "__main__":
    main()
    
