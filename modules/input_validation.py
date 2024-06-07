from rich.console import Console
from modules.helpers import is_data_valid


def user_input(label, available_options=None, description=None, type=None):
    console = Console()
    
    while True:
        user_prompt = input(label).strip()
        
        # Check length
        if len(user_prompt) > 20:
            console.print(f"[red bold]You cannot enter more than 20 characters")
        # Extra validation using is_data_valid helper if a type is provided
        # This also allows empty input necessary for the update_item function
        elif type:
            if is_data_valid(user_prompt, type):
                return user_prompt
            else:
                console.print(f"\n[red bold]The value must be {type}")
        # If the input is empty and there is a description provided, a warning is printed including the description
        elif user_prompt == "" and description:
            console.print(f"\n[red bold]{description} cannot be empty.")
        # If options are provided, the input validation is strict to options list
        elif available_options:
            if user_prompt not in available_options:
                console.print("[bold red]Please select one of the available options\n")
            else:
                return user_prompt
        else:
            return user_prompt