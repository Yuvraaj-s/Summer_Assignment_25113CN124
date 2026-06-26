# Write a program to Find pair with given sum

n = int(input("Enter number of elements: "))

arr = []

for i in range(n):
    x = int(input("Enter element: "))
    arr.append(x)

target = int(input("Enter the required sum: "))

found = 0

for i in range(n):
    for j in range(i + 1, n):
        if arr[i] + arr[j] == target:
            print("Pair found:", arr[i], arr[j])
            found = 1

if found == 0:
    print("No pair found")