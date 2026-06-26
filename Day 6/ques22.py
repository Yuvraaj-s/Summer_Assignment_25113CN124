# Write a program to Convert binary to decimal. 

b = input("Enter a binary number: ")

d = 0

for i in b:
    d = d * 2 + int(i)

print(d)