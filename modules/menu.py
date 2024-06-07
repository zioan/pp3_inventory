from rich.console import Console
from modules.input_validation import user_input
from modules.inventory_management import add_new_item, update_item, delete_item, search_inventory


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
    input = user_input("Choose an operation: ", choices)
    
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
      input = user_input("Choose an operation: ", choices)

      if input == "1":
          add_new_item()
      elif input == "2":
          update_item()
      elif input == "3":
          delete_item()
      elif input == "4":
          search_inventory()
      elif input == "0":
          return  # Return to the previous menu
        
     