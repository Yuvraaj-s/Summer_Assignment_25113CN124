# Write a program to Merge arrays.

n1 = int(input("Enter number of elements in first array: "))

arr1 = []

for i in range(n1):
    x = int(input("Enter element: "))
    arr1.append(x)

n2 = int(input("Enter number of elements in second array: "))

arr2 = []

for i in range(n2):
    x = int(input("Enter element: "))
    arr2.append(x)

arr3 = []

for i in range(n1):
    arr3.append(arr1[i])

for i in range(n2):
    arr3.append(arr2[i])

print("Merged array:")

for i in range(len(arr3)):
    print(arr3[i])