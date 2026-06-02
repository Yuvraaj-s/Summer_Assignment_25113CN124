# Write a program to Find product of digits.

pro = 1
n = int(input("Enter n : "))
while n>0 :
     
     d = int(n%10)
     if d==0 :
         break
     pro *= d
     n = n/10 
     
print("The product for the digidts of the given no. is = ",pro)