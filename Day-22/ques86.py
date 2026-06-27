# Write a program to Count words in a sentence. 

string = input("Enter a sentence: ")

count = 1

for i in string:
    if i == " ":
        count = count + 1

print("Number of words:", count)