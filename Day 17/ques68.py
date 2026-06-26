# Write a program to Find common elements.

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

print("Common elements are:")

for i in range(n1):
    for j in range(n2):
        if arr1[i] == arr2[j]:
            print(arr1[i])
            break