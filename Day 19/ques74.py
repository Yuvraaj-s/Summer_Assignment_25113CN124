# Write a program to Subtract matrices.

rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

matrix1 = []
matrix2 = []
result = []

print("Enter elements of first matrix:")

for i in range(rows):
    row = []
    for j in range(cols):
        x = int(input())
        row.append(x)
    matrix1.append(row)

print("Enter elements of second matrix:")

for i in range(rows):
    row = []
    for j in range(cols):
        x = int(input())
        row.append(x)
    matrix2.append(row)

for i in range(rows):
    row = []
    for j in range(cols):
        row.append(matrix1[i][j] - matrix2[i][j])
    result.append(row)

print("Difference of matrices:")

for i in range(rows):
    for j in range(cols):
        print(result[i][j], end=" ")
    print()