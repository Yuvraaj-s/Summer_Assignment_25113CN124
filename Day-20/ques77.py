# Write a program to Multiply matrices. .

rows1 = int(input("Enter rows of first matrix: "))
cols1 = int(input("Enter columns of first matrix: "))

matrix1 = []

print("Enter elements of first matrix:")

for i in range(rows1):
    row = []
    for j in range(cols1):
        x = int(input())
        row.append(x)
    matrix1.append(row)

rows2 = int(input("Enter rows of second matrix: "))
cols2 = int(input("Enter columns of second matrix: "))

matrix2 = []

print("Enter elements of second matrix:")

for i in range(rows2):
    row = []
    for j in range(cols2):
        x = int(input())
        row.append(x)
    matrix2.append(row)

result = []

for i in range(rows1):
    row = []
    for j in range(cols2):
        row.append(0)
    result.append(row)

for i in range(rows1):
    for j in range(cols2):
        for k in range(cols1):
            result[i][j] = result[i][j] + matrix1[i][k] * matrix2[k][j]

print("Product of matrices:")

for i in range(rows1):
    for j in range(cols2):
        print(result[i][j], end=" ")
    print()