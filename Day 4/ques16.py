# Write a program to Print Armstrong numbers in a range. 
m = int(input("Enter the first no. : "))
n = int(input("enter The 2nd no :"))

for i in range (m,n+1):
  s = 0
  t = i
  while t>0 :
    d = t%10
    s += d*d*d
    t = t//10
  if s == i:
       print(i)