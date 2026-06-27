# Write a program to Frequency of an element

n = int(input("Enter number of elements: "))

arr = []

for i in range(n):
    x = int(input("Enter element: "))
    arr.append(x)

key = int(input("Enter element to find frequency: "))

count = 0

for i in range(n):
    if arr[i] == key:
        count = count + 1

print("Frequency of", key, "is", count)