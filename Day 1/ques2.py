#Write a program to Print multiplication table of a given number. 

n = int(input("Enter the no. :"))
for i in range (1,11):
    pro= n*i
    print(f"{n}x{i}={pro}")