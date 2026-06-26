# Write a program to Check symmetric matrix.

n = int(input("Enter order of square matrix: "))

matrix = []

print("Enter elements of matrix:")

for i in range(n):
    row = []
    for j in range(n):
        x = int(input())
        row.append(x)
    matrix.append(row)

flag = 1

for i in range(n):
    for j in range(n):
        if matrix[i][j] != matrix[j][i]:
            flag = 0
            break

if flag == 1:
    print("Matrix is symmetric")
else:
    print("Matrix is not symmetric")