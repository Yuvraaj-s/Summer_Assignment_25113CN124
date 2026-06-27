# Write a program to Move zeroes to end.

n = int(input("Enter number of elements: "))

arr = []

for i in range(n):
    x = int(input("Enter element: "))
    arr.append(x)

new_arr = []

for i in range(n):
    if arr[i] != 0:
        new_arr.append(arr[i])

for i in range(n):
    if arr[i] == 0:
        new_arr.append(arr[i])

print("Array after moving zeroes to end:")

for i in range(n):
    print(new_arr[i])