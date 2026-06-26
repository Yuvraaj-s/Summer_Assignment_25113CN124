# Write a program to Find largest and smallest element. 

n = int(input("Enter number of elements: "))

arr = []

for i in range(n):
    x = int(input("Enter element: "))
    arr.append(x)

largest = arr[0]
smallest = arr[0]

for i in range(1, n):
    if arr[i] > largest:
        largest = arr[i]
    if arr[i] < smallest:
        smallest = arr[i]

print("Largest element:", largest)
print("Smallest element:", smallest)