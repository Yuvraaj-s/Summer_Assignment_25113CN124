import math
n = int(input("Enter the number: "))

temp = n
factS = 0

while temp > 0:
    d = temp % 10
    factS += math.factorial(d)
    temp //= 10

if factS == n:
    print(f"{n} is a Strong Number.")
else:
    print(f"{n} is NOT a Strong Number.")