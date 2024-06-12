# Inventory Management System

The Inventory Management System is a Python-based application designed to simplify the process of managing an inventory of items. Whether you're adding new items, updating existing ones, or deleting obsolete ones, this system provides a user-friendly interface to handle these tasks efficiently.


## Table of Contents

1. [User Stories](#user-stories)
2. [Features](#features)
    - [Main Menu](#main-menu)
    - [Operations Menu](#operations-menu)
    - [Add New Item](#add-new-item)
    - [Update Item](#update-item)
    - [Delete Item](#delete-item)
    - [Search Inventory](#search-inventory)
    - [Help Section](#help-section)
    - [Validation](#validation)
3. [How to Use](#how-to-use)
4. [User Benefits](#user-benefits)
5. [Logic Flow](#logic-flow)
6. [Data Model](#data-model)
7. [Libraries and Technologies Used](#libraries-and-technologies-used)
8. [Testing](#testing)
    - [Input Testing](#input-testing)
    - [PEP8 Testing](#pep8-testing)
    - [Testing User Stories](#testing-user-stories)
9. [Bugs](#bugs)
10. [Version Control](#version-control)
11. [Deployment](#deployment)
12. [Credits](#credits)


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


## Testing

The Inventory Management System undergoes rigorous testing to ensure functionality, reliability, and adherence to coding standards. Testing encompasses various aspects of the system, including input validation, compliance with PEP8 coding guidelines, and validation of user stories.

### Input Testing

Input testing focuses on validating user inputs to ensure that the system handles different scenarios gracefully and provides appropriate feedback to users. Key aspects of input testing include:

- **Boundary Testing**: Test inputs at the extremes of allowed ranges to verify that the system handles edge cases correctly.
  
- **Invalid Input Testing**: Test inputs with invalid formats or values to ensure that the system rejects them and provides informative error messages to users.

- **Empty Input Testing**: Test scenarios where required fields are left empty to ensure that the system prompts users to provide the necessary information and does not proceed with incomplete data.

- **Confirmation Testing**: Test confirmation prompts for operations such as adding, updating, or deleting items to ensure that users can confirm or cancel their actions as intended.

### PEP8 Testing

PEP8 testing focuses on ensuring that the codebase adheres to the guidelines outlined in PEP8, the official style guide for Python code. Key aspects of PEP8 testing include:

- **Code Formatting**: Verify that the code follows consistent formatting conventions, including indentation, line length, and spacing.

- **Naming Conventions**: Ensure that variable names, function names, and other identifiers adhere to PEP8 naming conventions to improve code readability and maintainability.

- **Code Structure**: Review the overall structure of the codebase to identify any potential improvements in organization and clarity.

- **Code Linting**: Utilize automated code analysis tools such as Flake8 or Pylint to identify and correct violations of PEP8 guidelines.

### Testing User Stories

Testing user stories involves verifying that the system's features and functionality align with user expectations and requirements. Key aspects of testing user stories include:

- **Scenario Testing**: Test each user story scenario to ensure that the system behaves as expected and meets user needs.

- **User Interaction Testing**: Evaluate user interactions with the system to identify any usability issues or areas for improvement.

- **Edge Case Testing**: Test user stories with edge cases to verify that the system handles uncommon or unexpected scenarios correctly.

By conducting thorough input testing, PEP8 testing, and testing of user stories, the Inventory Management System maintains high standards of quality, usability, and user satisfaction.


All Python files have been passed through [Code Institute PEP8 Validator](https://pep8ci.herokuapp.com/) to ensure compliance with PEP8 standards.


## Bugs

The following bugs were identified and fixed during the development stage:

1. **Fix delete function behavior when breaking the loop**: Resolved an issue where the delete function behavior was inconsistent when breaking the loop, ensuring that items are deleted correctly.

2. **Fix application not exiting and returning to main menu properly**: Addressed a bug where the application did not exit properly and return to the main menu after completing an operation, ensuring smooth navigation within the system. The characteristic of this bug was prompting the same menu for a second time before taking the proper action.

3. **Fix user_input validation to handle empty input and expected type in the same time**: Fixed a validation bug where the system did not handle empty input and expected type validation simultaneously, improving input validation and user experience. This feature is used in the update function.

4. **Fix search_inventory data retrieving after each operation**: Corrected an issue where the search_inventory function did not retrieve data correctly after performing an operation, ensuring accurate search results. In other words, the search functionality was serving outdated data.

There are no known unfixed bugs in the Inventory Management System.


## Version Control

Throughout the development process, I utilized basic Git commands to manage version control effectively. All necessary files were included in the repository. Here are the main commands I used:

- git add 'file_name': Added specific files to the staging area before committing changes.
- git add.: To add all files to the staging area before committing changes.
- git commit -m "commit message": Commited the staged changes with descriptive messages to track the progress of the project.
- git push: Pushed local commits to the remote repository on GitHub, ensuring that the latest changes were synchronized with the online repository.


## Deployment

I deployed the Inventory Management System using Heroku's dashboard, which provides a user-friendly interface for deploying web applications. Here's how I did it:

1. **Creating a Heroku App**: I logged in to my Heroku account and navigated to the dashboard. From there, I clicked on the "New" button and selected "Create new app". I entered a unique name for my app and chose the appropriate region.

2. **Connecting to GitHub**: In the deployment section of my Heroku app dashboard, I selected the deployment method as GitHub. I connected my GitHub account and selected the repository containing my Inventory Management System code.

6. **Configuring Environment Variables**: I configured any necessary environment variables in the Heroku dashboard under the "Settings" tab for my app.

5. **Installing Python and Node.js Buildpacks**: In the settings section of my Heroku app dashboard, I navigated to the "Buildpacks" section. From there, I added both the Python and Node.js Buildpacks to ensure that my application could handle both Python and JavaScript dependencies required for the template.

3. **Configuring Automatic Deploys**: After connecting to GitHub, I enabled automatic deploys for my app. This allowed Heroku to automatically deploy my application whenever I pushed changes to the connected GitHub repository.

4. **Manual Deployments**: Additionally, I had the option to manually trigger deployments from the dashboard. I could select a branch to deploy and initiate the deployment process with a simple click.

5. **Verifying Deployment**: Once the deployment process completed, I verified that my application was running smoothly by opening the provided Heroku URL in my web browser.

By following these steps through Heroku's dashboard, I successfully deployed the Inventory Management System, making it accessible to users.


## Credits

### Resources Used

- **Heroku**: The platform provided seamless deployment and hosting services for the application.

- **Google Sheets API**: Integration with the API enabled efficient data management and storage.

- **Rich Library**: The Rich library enhanced the terminal interface with colorful styling and table formatting.

- **gspread Library**: This library facilitated interaction with Google Sheets, allowing seamless data retrieval and manipulation.

- **Text to ASCII Art Generator**: ASCII art in the application was generated using the "text2art" library.

- **Prompt Toolkit Documentation**: For advanced input handling.

- **Stack Overflow**: For troubleshooting and code examples.

[Back to Top](#inventory-management-system)