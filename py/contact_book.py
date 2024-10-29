import os;
import json

saved_contacts = []
path = r"C:\Users\ander\Desktop\contacts.json.txt" # update this path to read from your local file 


def load_contacts():
    #Load contacts from the JSON file if it exists
    if os.path.exists(path):
        try:
            with open(path, "r") as file:
                global saved_contacts
                saved_contacts = json.load(file)
                print(f"Loaded {len(saved_contacts)} contacts.\n")
        except json.JSONDecodeError:
            print("File is empty or corrupted\n")
    else:
        print("No contacts found. Starting fresh.\n")

def save_contacts():
    """Save contacts to the JSON file."""
    try:
        with open(path, "w") as file:
            json.dump(saved_contacts, file, indent=4)
        print("Contacts saved successfully!\n")
    except Exception as e:
        print(f"An error occurred while saving contacts: {e}")       

def add_contact():
    first_name = input("Enter First name: ").strip()
    last_name = input("Enter Last name: ").strip()
    phone_number = int(input("Enter Phone Number: "))

    contact = {
        "first_name": first_name,
        "last_name": last_name,
        "phone_number": phone_number
    }
    
    print(f"The number {phone_number} will be saved as: {first_name} {last_name}")
    save_message = input("enter OK! to save: ").strip().lower()

    if save_message == "ok":
       saved_contacts.append(contact)
       save_contacts()
       print("Contact saved successfully!\n")
    elif save_message != "ok":
        print("Wrong specification")    
    else:
        print("Save canceled.\n")
        
def view_contacts():
    if saved_contacts:
        print("\nSaved Contacts: ")
        for contact in saved_contacts:
            print(f"{saved_contacts.index(contact) + 1}. {contact["first_name"]} {contact["last_name"]}")
    else:
        print("\nNo contacts saved yet") 
             
def update_contact():
    if not saved_contacts:
        print("\nNo contacts to update")
        return 
    view_contacts()
    try:
        contact_num = int(input("Enter the contact number to update: ")) - 1
        # updating a particular field
        if 0 <= contact_num < len(saved_contacts):
            print("What do you want to update")
            print("1. First name")
            print("2. Last name")
            print("3. Number")
            update_choice = input("Choose an option: ")
            
            if update_choice == "1":
                new_fn = input("Please the new first name: ").strip()
                saved_contacts[contact_num]["first_name"] = new_fn
                print("First name updated successfully!\n")
            elif update_choice == "2":
                new_ln = input("Please the new last name: ").strip()
                saved_contacts[contact_num]["last_name"] = new_ln
                print("Last name updated successfully!\n")
            elif update_choice == "3":    
                new_num = input("Please the new number: ").strip()
                saved_contacts[contact_num]["phone_number"] = new_num
                print("Number updated successfully!\n")
            else:
                print("Invalid option entered") 
                return
            save_contacts()   
    except:
        print("Error Updating the contact")
        
def delete_contact():
    if not saved_contacts:
        print("\nNo contacts to delete.")
        return

    view_contacts()
    try:
        contact_num = int(input("\nEnter the contact number to delete: ")) - 1
        if 0 <= contact_num < len(saved_contacts):
            deleted = saved_contacts.pop(contact_num)
            print(f"Deleted {deleted['first_name']} {deleted['last_name']} successfully!\n")
        else:
            print("Invalid contact number.\n")
    except ValueError:
        print("Please enter a valid number.\n")            


def main():
    print("Starting the contact book application...")  

    load_contacts() 
    while True:
        print("1. Add contact")
        print("2. View contacts")
        print("3. Update contact")
        print("4. Delete contact")
        print("5. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == "1":
            add_contact()
        elif choice == "2":
            print("-----------This are your saved contacts")
            view_contacts()
            print("---------------------------------")
        elif choice == "3":
            update_contact()
        elif choice == "4":
            delete_contact()        
        elif choice == "5":
            print("Exiting...........")
            break
        else:
            print("Invalid choice.")   

if __name__ == "__main__":
    main()                 
        