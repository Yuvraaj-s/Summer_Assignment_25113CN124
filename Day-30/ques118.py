# Write a program to Create mini library system
books = []

while True:
    print("\n--- Mini Library System ---")
    print("1. Add Book")
    print("2. Show Books")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        book = input("Enter book name: ")
        books.append(book)
        print("Book Added.")

    elif choice == 2:
        if len(books) == 0:
            print("No Books Available.")
        else:
            print("Books:")
            for i in books:
                print(i)

    elif choice == 3:
        book = input("Enter book name to issue: ")
        if book in books:
            books.remove(book)
            print("Book Issued.")
        else:
            print("Book Not Available.")

    elif choice == 4:
        book = input("Enter book name to return: ")
        books.append(book)
        print("Book Returned.")

    elif choice == 5:
        print("Thank You")
        break

    else:
        print("Invalid Choice")