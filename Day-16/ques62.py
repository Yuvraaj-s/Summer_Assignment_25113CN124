# Write a program to Find maximum frequency element

n = int(input("Enter number of elements: "))

arr = []

for i in range(n):
    x = int(input("Enter element: "))
    arr.append(x)

max_count = 0
max_element = arr[0]

for i in range(n):
    count = 0

    for j in range(n):
        if arr[i] == arr[j]:
            count = count + 1

    if count > max_count:
        max_count = count
        max_element = arr[i]

print("Maximum frequency element:", max_element)
print("Frequency:", max_count)