# Write a program to Create ticket booking system. 

tickets = 10

while True:
    print("\n--- Ticket Booking System ---")
    print("1. Book Ticket")
    print("2. Check Available Tickets")
    print("3. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        n = int(input("Enter number of tickets: "))

        if n <= tickets:
            tickets = tickets - n
            print("Ticket Booked.")
        else:
            print("Tickets Not Available.")

    elif choice == 2:
        print("Available Tickets =", tickets)

    elif choice == 3:
        print("Thank You")
        break

    else:
        print("Invalid Choice")