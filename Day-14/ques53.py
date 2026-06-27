# Write a program to Linear search. 



n = int(input("Enter number of elements: "))

arr = []

for i in range(n):
    x = int(input("Enter element: "))
    arr.append(x)

key = int(input("Enter element to search: "))

found = 0

for i in range(n):
    if arr[i] == key:
        print("Element found at position:", i + 1)
        found = 1
        break

if found == 0:
    print("Element not found")