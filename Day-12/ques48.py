# Write a program to Write function for perfect number.

def perfect(n):
    s = 0

    for i in range(1, n):
        if n % i == 0:
            s = s + i

    if s == n:
        print("Perfect Number")
    else:
        print("Not Perfect Number")

n = int(input("Enter a number: "))
perfect(n)