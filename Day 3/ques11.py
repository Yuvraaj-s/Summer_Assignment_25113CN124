# Write a program to Find GCD of two numbers

m = int(input("Enter m :"))
n = int(input("Enter n :"))

for i in range (min(m,n),2,-1):
    if n%i==0 | m%i==0 :

        print(i)

        break 