# Write a program to Find row-wise sum.

rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

matrix = []

print("Enter elements of matrix:")

for i in range(rows):
    row = []
    for j in range(cols):
        x = int(input())
        row.append(x)
    matrix.append(row)

print("Row-wise sum:")

for i in range(rows):
    sum = 0

    for j in range(cols):
        sum = sum + matrix[i][j]

    print("Sum of row", i + 1, "=", sum)