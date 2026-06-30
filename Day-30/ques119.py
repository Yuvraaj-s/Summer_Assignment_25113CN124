# Write a program to Create mini employee management system.
employees = []

while True:
    print("\n--- Mini Employee Management System ---")
    print("1. Add Employee")
    print("2. View Employees")
    print("3. Search Employee")
    print("4. Delete Employee")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        name = input("Enter employee name: ")
        employees.append(name)
        print("Employee Added.")

    elif choice == 2:
        if len(employees) == 0:
            print("No Employees Found.")
        else:
            print("Employee List:")
            for i in employees:
                print(i)

    elif choice == 3:
        name = input("Enter employee name: ")
        if name in employees:
            print("Employee Found.")
        else:
            print("Employee Not Found.")

    elif choice == 4:
        name = input("Enter employee name: ")
        if name in employees:
            employees.remove(name)
            print("Employee Deleted.")
        else:
            print("Employee Not Found.")

    elif choice == 5:
        print("Thank You")
        break

    else:
        print("Invalid Choice")