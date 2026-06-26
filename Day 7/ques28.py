# Write a program to Recursive reverse number. 

def reverse(n, rev):
    if n == 0:
        return rev
    return reverse(n // 10, rev * 10 + n % 10)

n = int(input("Enter a number: "))
print("Reverse =", reverse(n, 0))