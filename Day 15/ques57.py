# Write a program to Reverse array.

n = int(input("Enter number of elements: "))

arr = []

for i in range(n):
    x = int(input("Enter element: "))
    arr.append(x)

print("Reversed array:")

for i in range(n - 1, -1, -1):
    print(arr[i])