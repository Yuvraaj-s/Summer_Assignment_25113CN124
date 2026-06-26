# Write a program to Sort names alphabetically. 

n = int(input("Enter number of names: "))

names = []

for i in range(n):
    name = input("Enter name: ")
    names.append(name)

for i in range(n - 1):
    for j in range(n - 1 - i):
        if names[j] > names[j + 1]:
            temp = names[j]
            names[j] = names[j + 1]
            names[j + 1] = temp

print("Names in alphabetical order:")

for i in names:
    print(i)