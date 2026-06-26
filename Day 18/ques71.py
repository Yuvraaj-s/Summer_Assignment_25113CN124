# Write a program to Binary search. 

n = int(input("Enter number of elements: "))

arr = []

print("Enter elements in sorted order:")

for i in range(n):
    x = int(input("Enter element: "))
    arr.append(x)

key = int(input("Enter element to search: "))

low = 0
high = n - 1
found = 0

while low <= high:
    mid = (low + high) // 2

    if arr[mid] == key:
        print("Element found at position:", mid + 1)
        found = 1
        break

    elif key < arr[mid]:
        high = mid - 1

    else:
        low = mid + 1

if found == 0:
    print("Element not found")