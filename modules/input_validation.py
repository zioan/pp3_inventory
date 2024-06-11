from rich.console import Console


def user_input(label, available_options=None, type=None, allow_empty=False):
    console = Console()

    while True:
        user_prompt = input(label).strip()

        # Check if input length exceeds 20 characters
        if len(user_prompt) > 20:
            console.print("[red bold]You cannot enter more than 20 characters")
            continue  # Skip to the next iteration and prompt the user again

        # Check if input is not empty when empty strings are not allowed
        if not allow_empty and user_prompt == "":
            console.print("\n[red bold]This field cannot be empty.")
            continue  # Skip to the next iteration and prompt the user again

        # Validate input type
        if type and user_prompt and not is_data_valid(user_prompt, type):
            console.print(f"\n[red bold]The value must be {type}")
            continue  # Skip to the next iteration and prompt the user again

        # Validate against available options
        if available_options and user_prompt not in available_options:
            console.print("\n[bold red]Please select one available option")
            continue  # Skip to the next iteration and prompt the user again

        # If all checks pass, return the valid input
        return user_prompt


def is_data_valid(value, type):
    if type == "text":
        # Check if it's a string and not a numeric string
        return isinstance(value, str) and not value.isdigit()
    elif type == "positive number":
        try:
            # Check if it's a number and a positive number
            number = float(value)
            return number > 0
        except ValueError:
            return False
    return False  # If the type is neither "text" nor "positive number"
