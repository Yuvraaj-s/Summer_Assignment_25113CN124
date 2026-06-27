# Write a program to Check string rotation. 

string1 = input("Enter first string: ")
string2 = input("Enter second string: ")

temp = string1 + string1

if len(string1) == len(string2) and string2 in temp:
    print("Strings are rotations")
else:
    print("Strings are not rotations")