# Write a program to Find nth Fibonacci term. 

a = 0
b = 1

n = int(input("enter n :"))
for Series in range (n-1):
   
    s = a+b
    a = b
    b = s
    
print(a)