# Write a program to Check whether a number is palindrome. 

rev = 0
n = int(input("Enter n : "))
orig = n
while n>0 :
    d =  n%10 
    rev = rev*10 + d
    n = n//10
if   orig == rev :
    print("The no. is palindrome")
else :
    print ("the no. isn't palindrome ")