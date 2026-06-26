# Write a program to Write function to find maximum

def maximum(a, b):
    if a > b:
        return a
    else:
        return b

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

print("Maximum =", maximum(x, y))