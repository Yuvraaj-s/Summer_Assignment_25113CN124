# Write a program to Find LCM of two numbers. 

m = int(input("Enter the 1st number:"))
n = int(input("Enter the second number:"))


for i in range (max(m,n),m*n+1):
    if i%n ==0 | i%m== 0:

        print("LCM of the no.s",m,"&",n,"is",i)
        break 