# Write a program to Transpose matrix

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

print("Transpose of matrix:")

for i in range(cols):
    for j in range(rows):
        print(matrix[j][i], end=" ")
    print()