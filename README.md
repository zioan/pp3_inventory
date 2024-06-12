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


## Logic Flow

Starting with a flowchart helped to design the project efficiently. Flowcharts simplified the complex logic, making it easier to understand the code and identify potential error points.


## Data Model

The Inventory Management System utilizes a simple yet effective data model to store and manage inventory information. The data model consists of the following key components:

1. **Item**: Each inventory item is represented as a dictionary with the following attributes:
   - **Index**: A unique identifier for the item.
   - **Name**: The name of the item.
   - **Type**: The type or category of the item.
   - **Quantity**: The quantity or number of units available.
   - **Unit**: The unit of measurement for the item.

2. **Google Sheets Integration**: The system integrates with Google Sheets to store inventory data. Google Sheets provides a familiar and accessible platform for users to manage their inventory, offering features such as collaboration, version history, and easy access from any device with internet connectivity.

3. **Validation and Error Handling**: The system incorporates validation checks to ensure data integrity and accuracy. Input validation is performed for fields such as quantity and index to prevent incorrect or invalid data entry. Additionally, error handling mechanisms are implemented to gracefully handle exceptions and provide informative error messages to users in case of unexpected issues.

4. **Operations and CRUD Functionality**: The data model supports basic CRUD (Create, Read, Update, Delete) operations for managing inventory items. Users can add new items, update existing items, delete items, and view the current inventory. Each operation is designed to interact seamlessly with the underlying data model, ensuring consistent and reliable data management.

5. **Search Functionality**: The system includes a search feature that allows users to search for specific items by name. The search functionality enhances user experience by providing a quick and efficient way to locate inventory items without scrolling through the entire inventory list.

Overall, the data model of the Inventory Management System is designed to be flexible, scalable, and user-friendly, providing users with a robust platform for effective inventory management.


## Libraries and Technologies Used

The Inventory Management System leverages several libraries and technologies to provide a seamless user experience and efficient inventory management capabilities. Key components include:

1. **Python**: The system is built using Python, a versatile and widely-used programming language known for its simplicity and readability. Python provides the foundation for developing the application's logic and functionality.

2. **Rich Library**: Rich is a Python library that enhances terminal output with rich formatting, colors, and styles. It is utilized in the system's user interface to create visually appealing menus, tables, and text formatting, improving readability and user experience.

3. **gspread Library**: gspread is a Python library for accessing Google Sheets spreadsheets using the Google Sheets API. It enables seamless integration with Google Sheets, allowing the system to read and write inventory data to Google Sheets spreadsheets securely.

4. **Google Sheets API**: The Google Sheets API provides programmatic access to Google Sheets spreadsheets, allowing the system to interact with inventory data stored in Google Sheets. It facilitates real-time data synchronization, collaboration, and version control for inventory management.

5. **Text to ASCII Art Converter**: The system utilizes a text to ASCII art converter library to generate ASCII art for the welcome message, adding visual appeal to the user interface and enhancing the overall user experience.

By leveraging these libraries and technologies, the Inventory Management System delivers a robust, feature-rich solution for efficient inventory management in a terminal-based environment.
