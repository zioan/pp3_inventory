from rich.console import Console
from modules.input_validation import user_input


def convert_to_dict(data):
    """Convert data from Google Sheets API into a list of dictionaries.
    Args:
        data (list): A list of lists where the first sublist contains headers
                    and subsequent sublists contain inventory data.
    Returns:
        list: A list of dictionaries representing the inventory data.
    """
    # Extract the headers from the first row
    headers = data[0]
    # Initialize an empty list to store the dictionaries
    result = []
    # Iterate over each row in the data starting from the second row
    # Start from 1 to match Google Sheets row numbers
    for i, row in enumerate(data[1:], start=1):
        # Create a dictionary for the current row
        row_dict = {
            "index": i,  # Use the loop index as the row number.
            headers[0].lower(): row[0],  # "name"
            headers[1].lower(): row[1],  # "type"
            headers[2].lower(): row[2],  # "quantity", string
            headers[3].lower(): row[3]   # "unit"
        }
        # Add the dictionary to the result list
        result.append(row_dict)

    return result


def is_operation_canceled(user_input, cancel_value):
    console = Console()
    if user_input.lower() == cancel_value:
        console.print("[yellow]Operation aborted!\n")
        return True
    return False


def get_valid_index(data, prompt):
    console = Console()
    max_index = len(data)

    while True:
        index = user_input(f"{prompt} (1 - {max_index}): ")

        # Abort operation if user cancels
        if is_operation_canceled(index, "c"):
            return None

        try:
            index = int(index)
            if index not in range(1, max_index + 1):
                index_warning = f"Index should be between 1 and {max_index}."
                console.print(f"[red]Invalid index '{index}'. {index_warning}")
                continue
        except ValueError:
            number_warning = "Please enter a number."
            console.print(f"[red]Invalid input '{index}'. {number_warning}")
            continue

        return index
