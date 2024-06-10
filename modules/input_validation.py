from rich.console import Console


def user_input(label, available_options=None, description=None, expected_type=None, allow_empty=False):
    console = Console()
    
    while True:
        user_prompt = input(label).strip()
        
        # Check if input length exceeds 20 characters
        if len(user_prompt) > 20:
            console.print(f"[red bold]You cannot enter more than 20 characters")
            continue  # Skip to the next iteration of the loop to prompt the user again
        
        # Check if input is not empty when empty strings are not allowed
        if not allow_empty and user_prompt == "":
            console.print(f"\n[red bold]{description} cannot be empty.")
            continue  # Skip to the next iteration of the loop to prompt the user again
        
        # Validate input type
        if expected_type and not is_data_valid(user_prompt, expected_type):
            console.print(f"[red bold]The value must be {expected_type}")
            continue  # Skip to the next iteration of the loop to prompt the user again
        
        # Validate against available options
        if available_options and user_prompt not in available_options:
            console.print("[bold red]Please select one of the available options\n")
            continue  # Skip to the next iteration of the loop to prompt the user again
        
        # If all checks pass, return the valid input
        return user_prompt

    
def is_data_valid(value, expected_type):
    if expected_type == "text":
        # Check if it's a string and not a numeric string
        return isinstance(value, str) and not value.isdigit()
    elif expected_type == "positive number":
        try:
            # Check if it's a number and a positive number
            number = float(value)
            return number > 0
        except ValueError:
            return False
    return False  # If the expected_type is neither "text" nor "positive number"