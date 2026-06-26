# Write a program to Check perfect number

n = int(input("Enter the number : "))

if n <= 0:
    print(f"{n} is NOT a Perfect Number")
else:
    
    s = 0
    for i in range(1, n):
        if n % i == 0:
            s += i
            
    if s == n:
        print(f"{n} is a Perfect Number.")
    else:
        print(f"{n} is NOT a Perfect Number.")