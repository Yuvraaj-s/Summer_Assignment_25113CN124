# Write a program to Create student record system using arrays and strings. 
names = []
marks = []

while True:
    print("\n--- Student Record System ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        name = input("Enter student name: ")
        mark = int(input("Enter marks: "))
        names.append(name)
        marks.append(mark)
        print("Student Record Added.")

    elif choice == 2:
        if len(names) == 0:
            print("No Records Found.")
        else:
            print("Student Records:")
            for i in range(len(names)):
                print(names[i], "-", marks[i])

    elif choice == 3:
        name = input("Enter student name: ")
        if name in names:
            index = names.index(name)
            print("Marks =", marks[index])
        else:
            print("Student Not Found.")

    elif choice == 4:
        name = input("Enter student name: ")
        if name in names:
            index = names.index(name)
            names.pop(index)
            marks.pop(index)
            print("Student Record Deleted.")
        else:
            print("Student Not Found.")

    elif choice == 5:
        print("Thank You")
        break

    else:
        print("Invalid Choice")