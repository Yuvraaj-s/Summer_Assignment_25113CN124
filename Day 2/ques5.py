# Write a program to Find sum of digits of a number. 

sUM = 0
n = int(input("Enter n:"))
while n > 0 :
    d = int(n %10)
    sUM += d
    n = n/10
print("The sum of the digits of the given no. is =",sUM) 