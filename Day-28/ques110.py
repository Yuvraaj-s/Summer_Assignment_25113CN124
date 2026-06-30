# Write a program to Create bank account system. 
balance = 0

while True:
    print("\n   Bank Account System   ")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        amount = int(input("Enter amount to deposit: "))
        balance = balance + amount
        print("Amount Deposited.")

    elif choice == 2:
        amount = int(input("Enter amount to withdraw: "))
        if amount <= balance:
            balance = balance - amount
            print("Amount Withdrawn.")
        else:
            print("Insufficient Balance.")

    elif choice == 3:
        print("Current Balance =", balance)

    elif choice == 4:
        print("Thank You")
        break

    else:
        print("Invalid Choice")