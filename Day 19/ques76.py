# Write a program to Find diagonal sum.

n = int(input("Enter order of square matrix: "))

matrix = []

print("Enter elements of matrix:")

for i in range(n):
    row = []
    for j in range(n):
        x = int(input())
        row.append(x)
    matrix.append(row)

sum = 0

for i in range(n):
    sum = sum + matrix[i][i]

print("Sum of diagonal elements:", sum)