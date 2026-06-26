# Write a program to Write function to check prime. 
def prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

n = int(input("Enter a number: "))

if prime(n):
    print("Prime Number")
else:
    print("Not Prime Number")