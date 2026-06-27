# Write a program to Check palindrome string.

string = input("Enter a string: ")

reverse = ""

for i in string:
    reverse = i + reverse

if string == reverse:
    print("String is palindrome")
else:
    print("String is not palindrome")