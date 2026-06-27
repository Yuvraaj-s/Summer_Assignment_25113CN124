# Write a program to Create student record management system

students = []

while True:
    print("\n===== STUDENT RECORD MENU =====")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        name = input("Enter student name: ")
        roll = input("Enter roll number: ")
        marks = int(input("Enter marks: "))

        students.append([name, roll, marks])

        print("Student record added successfully.")

    elif choice == 2:
        print("\nStudent Records:")

        for i in students:
            print("Name:", i[0])
            print("Roll No:", i[1])
            print("Marks:", i[2])
            print()

    elif choice == 3:
        print("Exiting...")
        break

    else:
        print("Invalid choice")