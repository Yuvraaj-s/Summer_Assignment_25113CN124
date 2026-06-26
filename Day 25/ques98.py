# Write a program to Find common characters in strings.

string1 = input("Enter first string: ")
string2 = input("Enter second string: ")

result = ""

for i in string1:
    if i in string2 and i not in result:
        result = result + i

print("Common characters:", result)