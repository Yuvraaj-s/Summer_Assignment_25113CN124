# Write a program to Develop complete mini project using arrays, strings and functions
names = []
marks = []

def add_student():
    name = input("Enter student name: ")
    mark = int(input("Enter marks: "))
    names.append(name)
    marks.append(mark)
    print("Student Added.")

def view_students():
    if len(names) == 0:
        print("No Records Found.")
    else:
        print("\nStudent Records")
        for i in range(len(names)):
            print(names[i], "-", marks[i])

def search_student():
    name = input("Enter student name: ")

    if name in names:
        index = names.index(name)
        print("Marks =", marks[index])
    else:
        print("Student Not Found.")

def delete_student():
    name = input("Enter student name: ")

    if name in names:
        index = names.index(name)
        names.pop(index)
        marks.pop(index)
        print("Student Deleted.")
    else:
        print("Student Not Found.")

while True:
    print("\n--- Student Management System ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        add_student()

    elif choice == 2:
        view_students()

    elif choice == 3:
        search_student()

    elif choice == 4:
        delete_student()

    elif choice == 5:
        print("Thank You")
        break

    else:
        print("Invalid Choice")