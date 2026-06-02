# Write a program to Reverse a number.

rev = 0
n = int(input("Enter n : "))
while n>0 :
    d =  n%10 
    rev = rev*10 + d
    n = n//10
print("The reverse of the no. is : ",rev)

