# Write a program to Input and display array.

'''I'm using the concept the lists to
 solve these types of problems .'''


n = int(input("Enter number of elements: "))

arr = []

for i in range(n):
    x = int(input("Enter element: "))
    arr.append(x)

print("Array elements are:")

for i in range(n):
    print(arr[i])

