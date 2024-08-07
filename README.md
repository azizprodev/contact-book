# Contact Book

A simple console-based contact book application in Python that allows users to add, edit, delete, search, and display contacts.
The contacts are saved in a JSON file for persistent storage.

## Features

- Add new contacts
- Edit existing contacts
- Delete contacts
- Search for contacts
- Display all contacts

## Getting Started

### Prerequisites

- Python 3.x

### Installation

1. Clone the repository:

- git clone https://github.com/azizprodev/contact-book.git
  
2. Navigate
- cd contact-book

### Usage
- python main.py

### Functions

**load_contacts()**
Loads contacts from the contacts.json file.

**save_contacts(contacts)**
Saves the contacts to the contacts.json file.

**add_contact(contacts)**
Prompts the user to enter a contact name and number, and adds the contact to the dictionary.

**edit_contact(contacts)**
Prompts the user to enter the name of the contact to edit and the new contact number.

**delete_contact(contacts)**
Prompts the user to enter the name of the contact to delete.

**search_contact(contacts)**
Prompts the user to enter the name of the contact to search for and displays the contact if found.

**display_contacts(contacts)**
Displays all saved contacts.

### Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.
