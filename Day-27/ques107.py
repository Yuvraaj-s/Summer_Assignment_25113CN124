# Write a program to Create salary management system. 

employees = []

while True:
    print("\n===== SALARY MANAGEMENT MENU =====")
    print("1. Add Employee")
    print("2. Display Salary Details")
    print("3. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        name = input("Enter employee name: ")
        emp_id = input("Enter employee ID: ")
        basic = int(input("Enter basic salary: "))
        hra = int(input("Enter HRA: "))
        da = int(input("Enter DA: "))

        total_salary = basic + hra + da

        employees.append([name, emp_id, basic, hra, da, total_salary])

        print("Employee salary record added successfully.")

    elif choice == 2:
        print("\nSalary Details:")

        for i in employees:
            print("Name:", i[0])
            print("Employee ID:", i[1])
            print("Basic Salary:", i[2])
            print("HRA:", i[3])
            print("DA:", i[4])
            print("Total Salary:", i[5])
            print()

    elif choice == 3:
        print("Exiting system...")
        break

    else:
        print("Invalid choice")