# Write a program to Find column-wise sum. 

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

print("Column-wise sum:")

for j in range(cols):
    sum = 0

    for i in range(rows):
        sum = sum + matrix[i][j]

    print("Sum of column", j + 1, "=", sum)