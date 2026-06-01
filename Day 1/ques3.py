#Write a program to Find factorial of a number.
n = int(input("Enter The no. :"))
fact = 1
for i in range (1,n+1):
    fact*=i
print("Factorial for the given no. is:",fact)