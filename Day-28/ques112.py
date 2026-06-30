# Write a program to Create contact management system. 
contacts = {}

while True:
    print("\n--- Contact Management System ---")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        name = input("Enter name: ")
        number = input("Enter phone number: ")
        contacts[name] = number
        print("Contact Added.")

    elif choice == 2:
        if len(contacts) == 0:
            print("No Contacts Found.")
        else:
            print("Contacts:")
            for i in contacts:
                print(i, "-", contacts[i])

    elif choice == 3:
        name = input("Enter name to search: ")
        if name in contacts:
            print("Phone Number =", contacts[name])
        else:
            print("Contact Not Found.")

    elif choice == 4:
        name = input("Enter name to delete: ")
        if name in contacts:
            del contacts[name]
            print("Contact Deleted.")
        else:
            print("Contact Not Found.")

    elif choice == 5:
        print("Thank You")
        break

    else:
        print("Invalid Choice")