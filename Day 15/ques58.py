# Write a program to Rotate array left

n = int(input("Enter number of elements: "))

arr = []

for i in range(n):
    x = int(input("Enter element: "))
    arr.append(x)

first = arr[0]

for i in range(n - 1):
    arr[i] = arr[i + 1]

arr[n - 1] = first

print("Array after left rotation:")

for i in range(n):
    print(arr[i])