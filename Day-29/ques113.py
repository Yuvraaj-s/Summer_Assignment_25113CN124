# Write a program to Create menu-driven calculator. 

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

while True:
    print("\n--- Calculator ---")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("Answer =", num1 + num2)

    elif choice == 2:
        print("Answer =", num1 - num2)

    elif choice == 3:
        print("Answer =", num1 * num2)

    elif choice == 4:
        if num2 != 0:
            print("Answer =", num1 / num2)
        else:
            print("Division by zero is not possible.")

    elif choice == 5:
        print("Thank You")
        break

    else:
        print("Invalid Choice")