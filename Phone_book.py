print("----------Phone Book----------\n\n")
contact = {}

def display(contact):
    print("The Names and The Contact No. are :")
    for key in contact:
         print(f"{key} -- {contact.get(key)}")


while True:
    choice = int(input("Enter your choice\n 1 - Add\n 2 - Search\n 3 - Display All\n 4 - Edit\n 5 - Delete\n 6 - Exit:\n "))
    if choice == 1:
        name = input("Enter the contact name: ")
        phone_number = input("Enter the mobile number: ")
        contact[name] = phone_number
    elif choice == 2:
        search_name = input("Enter the contact name to search: ")
        if search_name in contact:
            print(search_name, ":", contact[search_name])
    elif choice == 3:
        display(contact)
    elif contact == 5:
        edit_contact_name = input("Enter the contact name to be edited: ")
        if edit_contact_name in contact:
            new_phone_number = input("Enter the new mobile number: ")
            contact[edit_contact_name] = new_phone_number
            print("Contact updated")
            display(contact)
        else:
            print("Name not found in contact book")
    elif contact == 5:
        # Delete a contact
        delete_contact_name = input("Enter the contact name to be deleted: ")
        if delete_contact_name in contact:
            confirm = input("Do you want to delete this contact (y/n): ")
            if confirm.lower() == 'y':
                del contact[delete_contact_name]
                print("Contact deleted")
                display(contact)
            else:
                print("Contact not deleted")
        else:
            print("Name not found in contact book")
    elif choice == 6:
        break
    else:
        print("Invalid choice")