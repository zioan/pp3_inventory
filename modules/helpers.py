from rich.console import Console


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
    for i, row in enumerate(data[1:], start=1): # Start from 1 to match Google Sheets row numbers
        # Create a dictionary for the current row
        row_dict = {
            "index": i, # Use the loop index as the row number. "index", number
            headers[0].lower(): row[0],  # "name"
            headers[1].lower(): row[1],  # "type"
            headers[2].lower(): row[2],  # "quantity", string
            headers[3].lower(): row[3]   # "unit"
        }
        # Add the dictionary to the result list
        result.append(row_dict)
    
    return result 


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
    else:
        # If the expected_type is neither "string" nor "number", return False
        return False
    

def is_operation_canceled(user_input, cancel_value):
    console = Console()
    if user_input.lower() == cancel_value:
        console.print("[yellow]Operation aborted!\n")
        return True
    return False