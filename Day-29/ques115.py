# Write a program to Create menu-driven string operations system. 
s = input("Enter a string: ")

while True:
    print("\n--- String Operations ---")
    print("1. Display String")
    print("2. Find Length")
    print("3. Convert to Uppercase")
    print("4. Convert to Lowercase")
    print("5. Reverse String")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("String =", s)

    elif choice == 2:
        print("Length =", len(s))

    elif choice == 3:
        print("Uppercase =", s.upper())

    elif choice == 4:
        print("Lowercase =", s.lower())

    elif choice == 5:
        print("Reverse =", s[::-1])

    elif choice == 6:
        print("Thank You")
        break

    else:
        print("Invalid Choice")