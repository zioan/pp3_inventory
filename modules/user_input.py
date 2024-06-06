from rich.console import Console
from modules.helpers import is_data_valid


def user_input(label, available_options=None, description=None, type=None):
    console = Console()
    
    while True:
        user_prompt = input(label).strip()
        
        if user_prompt == "" and description:
            console.print(f"\n[red bold]{description} cannot be empty.")
        elif len(user_prompt) > 20:
            console.print(f"[red bold]You cannot enter more than 20 characters")
        elif type:
            if is_data_valid(user_prompt, type):
                return user_prompt
            else:
                console.print(f"\n[red bold]The value must be {type}")
        elif available_options:  # If available_options is not empty
            if user_prompt not in available_options:
                console.print("[bold red]Please select one of the available options\n")
            else:
                return user_prompt
        else:  # If available_options is empty
            return user_prompt
