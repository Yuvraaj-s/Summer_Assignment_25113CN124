#Write a program to Calculate sum of first N natural numbers.
sum = 0
num = int(input("Enter the no. :"))

for i in range (1,num+1):
    sum += i
print("The sum of no.s upto the  given no. =",sum)