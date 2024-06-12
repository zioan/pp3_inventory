# Inventory Management System

The Inventory Management System is a Python-based application designed to simplify the process of managing an inventory of items. Whether you're adding new items, updating existing ones, or deleting obsolete ones, this system provides a user-friendly interface to handle these tasks efficiently.

## User Stories

As a user, I want to be able to:
- view the current inventory items and search for specific items to quickly find what I need.
- perform various operations on inventory items, such as adding, updating, and deleting items, so that I can keep my inventory accurate and up-to-date.
- receive help and guidance on how to use the application, ensuring that I can navigate through its features smoothly.
- exit the application easily when I'm done using it, providing a seamless user experience.


## Features

### Main Menu
- Provides options to navigate through the application.
- Allows users to view inventory items, perform operations, access help, and exit the application.

### Operations Menu
- Offers a range of operations for managing inventory items, including adding, updating, deleting, and searching for items.
- Guides users through each operation with clear prompts and instructions.

#### Add New Item
- Allows users to add a new item to the inventory.
- Prompts users to enter details such as name, type, quantity, and unit.
- Validates input and provides options to cancel the operation if needed.

#### Update Item
- Enables users to update an existing item in the inventory.
- Prompts users to select the item to update and enter new details for each attribute.
- Validates input and provides options to cancel the operation if needed.

#### Delete Item
- Allows users to delete an item from the inventory.
- Prompts users to select the item to delete and confirms the deletion before proceeding.

#### Search Inventory
- Enables users to search for items in the inventory by name.
- Displays search results and provides options to perform other operations such as adding, updating, or deleting items.
- Runs in a loop until the user decides to return to the main menu.

### Help Section
- Provides comprehensive instructions and guidance on how to use the application effectively.
- Offers explanations for each menu option, including examples and tips for better clarity.
- Ensures users have access to assistance whenever needed.

### Validation
- Implements robust input validation to ensure data integrity and prevent errors.
- Checks for valid input types, empty values, and available options to enhance user experience.
