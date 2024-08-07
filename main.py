import json

# File where contacts will be stored
CONTACTS_FILE = "contacts.json"

# Load contacts from file
def load_contacts():
    try:
        with open(CONTACTS_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        return {}

# Save contacts to file
def save_contacts(contacts):
    with open(CONTACTS_FILE, 'w') as file:
        json.dump(contacts, file)

# Add a new contact
def add_contact(contacts):
    name = input("Enter contact name: ")
    number = input("Enter contact number: ")
    contacts[name] = number
    save_contacts(contacts)
    print(f"Contact {name} added.")

# Edit an existing contact
def edit_contact(contacts):
    name = input("Enter the name of the contact to edit: ")
    if name in contacts:
        new_number = input("Enter new contact number: ")
        contacts[name] = new_number
        save_contacts(contacts)
        print(f"Contact {name} updated.")
    else:
        print("Contact not found.")

# Delete a contact
def delete_contact(contacts):
    name = input("Enter the name of the contact to delete: ")
    if name in contacts:
        del contacts[name]
        save_contacts(contacts)
        print(f"Contact {name} deleted.")
    else:
        print("Contact not found.")

# Search for a contact
def search_contact(contacts):
    name = input("Enter the name of the contact to search: ")
    if name in contacts:
        print(f"{name}: {contacts[name]}")
    else:
        print("Contact not found.")

# Display all contacts
def display_contacts(contacts):
    if contacts:
        print("\n****** Saved Contacts ******")
        for name, number in contacts.items():
            print(f"{name}: {number}")
    else:
        print("No contacts found.")

# Main function
def main():
    contacts = load_contacts()
    
    while True:
        print("\n****** Contact Book ******")
        print("1. Add Contact")
        print("2. Edit Contact")
        print("3. Delete Contact")
        print("4. Search Contact")
        print("5. Display All Contacts")
        print("6. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            edit_contact(contacts)
        elif choice == '3':
            delete_contact(contacts)
        elif choice == '4':
            search_contact(contacts)
        elif choice == '5':
            display_contacts(contacts)
        elif choice == '6':
            print("Exiting the Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
