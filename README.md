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

## How to Use

1. **View Inventory**: Select "View Inventory" from the main menu to display all items currently in the inventory.

2. **Add Item**:
   - Choose "Add" from the Operations Menu.
   - Enter the details of the new item, including name, type, quantity, and unit.
   - Confirm to save the new item to the inventory.

3. **Update Item**:
   - Select "Update" from the Operations Menu to modify an existing item.
   - Enter the index of the item you want to update.
   - Modify the details of the item, including name, type, quantity, and unit.
   - Leave the input empty for any detail you don't want to change, keeping the previous value unchanged.
   - Confirm to save the changes to the inventory.

4. **Delete Item**:
   - Choose "Delete" from the Operations Menu to remove an item from the inventory.
   - Enter the index of the item you want to delete.
   - Confirm the deletion to remove the item from the inventory.

5. **Search Inventory**:
   - Access the "Search" option from the Operations Menu to quickly locate specific items.
   - Enter the name of the item you want to search for.
   - View the search results.
   - Choose to add, update, or delete items directly from the search results, enhancing user experience by providing context for the operations.


## User Benefits

The Inventory Management System significantly streamlines inventory management for users. Key benefits include:

- **Efficiency**: Manage inventory items efficiently through a user-friendly interface, reducing the time and effort required for inventory management tasks.
  
- **Accuracy**: Ensure data accuracy with built-in validation checks, preventing errors in data entry and ensuring reliable inventory records.

- **Control**: Perform operations such as adding, updating, and deleting items with confidence. Confirmation prompts during these operations help prevent accidental changes, giving users greater control over their inventory.

- **Convenience**: Search for items easily and manage them directly from the search results. This feature enhances user experience by providing a seamless workflow, allowing users to quickly locate and manage inventory items without navigating through multiple menus.

