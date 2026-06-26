# Write a program to Count set bits in a number. 

n = int(input("Enter a number: "))

count = 0

while n:
    count += n % 2
    n //= 2

print(count)