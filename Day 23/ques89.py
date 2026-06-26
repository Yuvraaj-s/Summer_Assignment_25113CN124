# Write a program to Find first non-repeating character.


string = input("Enter a string: ")

found = 0

for i in string:
    count = 0

    for j in string:
        if i == j:
            count = count + 1

    if count == 1:
        print("First non-repeating character:", i)
        found = 1
        break

if found == 0:
    print("No non-repeating character found")