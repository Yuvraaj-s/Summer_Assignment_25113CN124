# Write a program to Find missing number in array. 

n = int(input("Enter the value of n: "))

arr = []

print("Enter", n - 1, "elements:")

for i in range(n - 1):
    x = int(input("Enter element: "))
    arr.append(x)

for i in range(1, n + 1):
    found = 0

    for j in range(n - 1):
        if arr[j] == i:
            found = 1
            break

    if found == 0:
        print("Missing number is:", i)
        break