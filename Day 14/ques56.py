# Write a program to Find duplicates in array. 

n = int(input("Enter number of elements: "))

arr = []

for i in range(n):
    x = int(input("Enter element: "))
    arr.append(x)

print("Duplicate elements are:")

for i in range(n):
    for j in range(i + 1, n):
        if arr[i] == arr[j]:
            print(arr[i])
            break