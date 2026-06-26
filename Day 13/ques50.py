# Write a program to Find sum and average of array. 

'''I'm using the concept the lists to
 solve these types of problems .'''

n = int(input("Enter number of elements: "))

arr = []

for i in range(n):
    x = int(input("Enter element: "))
    arr.append(x)

total = 0

for i in range(n):
    total = total + arr[i]

average = total / n

print("Sum of array:", total)
print("Average of array:", average)