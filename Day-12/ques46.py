# Write a program to Write function for Armstrong

def armstrong(n):
    temp = n
    s = 0

    while n > 0:
        r = n % 10
        s = s + r ** 3
        n = n // 10

    if temp == s:
        print("Armstrong Number")
    else:
        print("Not Armstrong Number")

n = int(input("Enter a number: "))
armstrong(n)