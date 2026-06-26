# Write a program to Count even and odd elements. 

n = int(input("Enter number of elements: "))

arr = []

for i in range(n):
    x = int(input("Enter element: "))
    arr.append(x)

even_count = 0
odd_count = 0

for i in range(n):
    if arr[i] % 2 == 0:
        even_count = even_count + 1
    else:
        odd_count = odd_count + 1

print("Even elements count:", even_count)
print("Odd elements count:", odd_count)