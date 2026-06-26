# Write a program to Write function for palindrome. 

def palindrome(n):
    rev = 0
    temp = n

    while n > 0:
        rev = rev * 10 + n % 10
        n = n // 10

    if temp == rev:
        return True
    else:
        return False

n = int(input("Enter a number: "))

if palindrome(n):
    print("Palindrome")
else:
    print("Not Palindrome")
    