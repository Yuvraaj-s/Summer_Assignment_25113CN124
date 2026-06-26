# Write a program to Create employee management system. 

employees = []

while True:
    print("\n===== EMPLOYEE MANAGEMENT MENU =====")
    print("1. Add Employee")
    print("2. Display Employees")
    print("3. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        name = input("Enter employee name: ")
        emp_id = input("Enter employee ID: ")
        salary = int(input("Enter salary: "))

        employees.append([name, emp_id, salary])

        print("Employee added successfully.")

    elif choice == 2:
        print("\nEmployee Records:")

        for i in employees:
            print("Name:", i[0])
            print("Employee ID:", i[1])
            print("Salary:", i[2])
            print()

    elif choice == 3:
        print("Exiting system...")
        break

    else:
        print("Invalid choice")