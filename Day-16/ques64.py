# Write a program to Remove duplicates from array

n = int(input("Enter number of elements: "))

arr = []
new_arr = []

for i in range(n):
    x = int(input("Enter element: "))
    arr.append(x)

for i in range(n):
    found = 0

    for j in range(len(new_arr)):
        if arr[i] == new_arr[j]:
            found = 1
            break

    if found == 0:
        new_arr.append(arr[i])

print("Array after removing duplicates:")

for i in range(len(new_arr)):
    print(new_arr[i])