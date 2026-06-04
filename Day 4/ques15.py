# Write a program to Check Armstrong number.

n = int(input("enter n :"))
t = n
s = 0

while t>0 :
    d = t%10
    s += d*d*d
    t = t//10
if s == n:
      print("The no. is Armstrong")

else :
   print ("The no. isn't armstrong")