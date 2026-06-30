# Write a program to Create library management system. 
books = []

while True:
    print("\n--- Library Management System ---")
    print("1. Add Book")
    print("2. View Books")
    print("3. Remove Book")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        book = input("Enter book name: ")
        books.append(book)
        print("Book Added.")

    elif choice == 2:
        if len(books) == 0:
            print("No books available.")
        else:
            print("Books in Library:")
            for i in books:
                print(i)

    elif choice == 3:
        book = input("Enter book name to remove: ")
        if book in books:
            books.remove(book)
            print("Book Removed.")
        else:
            print("Book Not Found.")

    elif choice == 4:
        print("Thank You")
        break

    else:
        print("Invalid Choice")