# Write a program to Union of arrays. 

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

union = []

# Add elements of first array
for i in range(n1):
    union.append(arr1[i])

# Add only unique elements from second array
for i in range(n2):
    found = 0

    for j in range(len(union)):
        if arr2[i] == union[j]:
            found = 1
            break

    if found == 0:
        union.append(arr2[i])

print("Union of arrays:")

for i in range(len(union)):
    print(union[i])