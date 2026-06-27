b = input("Enter a binary number: ")

d = 0
p = 0

for i in range(len(b) - 1, -1, -1):
    d = d + int(b[i]) * (2 ** p)
    p = p + 1

print("Decimal =", d)