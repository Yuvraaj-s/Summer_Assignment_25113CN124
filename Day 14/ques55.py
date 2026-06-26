# Write a program to Second largest element. 

n = int(input("Enter number of elements: "))

arr = []

for i in range(n):
    x = int(input("Enter element: "))
    arr.append(x)

largest = arr[0]
second = arr[0]

# Find largest element
for i in range(n):
    if arr[i] > largest:
        largest = arr[i]

# Find second largest element
for i in range(n):
    if arr[i] > second and arr[i] < largest:
        second = arr[i]

print("Second largest element:", second)