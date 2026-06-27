# Write a program to Create marksheet generation system. 

students = []

while True:
    print("\n===== MARKSHEET MENU =====")
    print("1. Add Student Marks")
    print("2. Display Marksheet")
    print("3. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        name = input("Enter student name: ")
        roll = input("Enter roll number: ")

        m1 = int(input("Enter marks of Subject 1: "))
        m2 = int(input("Enter marks of Subject 2: "))
        m3 = int(input("Enter marks of Subject 3: "))

        total = m1 + m2 + m3
        percentage = total / 3

        if percentage >= 90:
            grade = "A+"
        elif percentage >= 75:
            grade = "A"
        elif percentage >= 60:
            grade = "B"
        elif percentage >= 40:
            grade = "C"
        else:
            grade = "Fail"

        students.append([name, roll, m1, m2, m3, total, percentage, grade])

        print("Marksheet data added successfully.")

    elif choice == 2:
        print("\n===== STUDENT MARKSHEET =====")

        for i in students:
            print("Name:", i[0])
            print("Roll No:", i[1])
            print("Subject 1:", i[2])
            print("Subject 2:", i[3])
            print("Subject 3:", i[4])
            print("Total Marks:", i[5])
            print("Percentage:", i[6])
            print("Grade:", i[7])
            print()

    elif choice == 3:
        print("Exiting system...")
        break

    else:
        print("Invalid choice")