# Write a program to Create inventory management system. 
items = {}

while True:
    print("\n--- Inventory Management System ---")
    print("1. Add Item")
    print("2. View Items")
    print("3. Search Item")
    print("4. Delete Item")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        name = input("Enter item name: ")
        qty = int(input("Enter quantity: "))
        items[name] = qty
        print("Item Added.")

    elif choice == 2:
        if len(items) == 0:
            print("Inventory is Empty.")
        else:
            print("Items in Inventory:")
            for i in items:
                print(i, "-", items[i])

    elif choice == 3:
        name = input("Enter item name: ")
        if name in items:
            print("Quantity =", items[name])
        else:
            print("Item Not Found.")

    elif choice == 4:
        name = input("Enter item name: ")
        if name in items:
            del items[name]
            print("Item Deleted.")
        else:
            print("Item Not Found.")

    elif choice == 5:
        print("Thank You")
        break

    else:
        print("Invalid Choice")