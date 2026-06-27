# Write a program to Merge two sorted arrays. 

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

arr = []

for i in arr1:
    arr.append(i)

for i in arr2:
    arr.append(i)

n = len(arr)

for i in range(n - 1):
    for j in range(n - 1 - i):
        if arr[j] > arr[j + 1]:
            temp = arr[j]
            arr[j] = arr[j + 1]
            arr[j + 1] = temp

print("Merged sorted array:")

for i in arr:
    print(i)