# Write a program to Find longest word. 

string = input("Enter a sentence: ")

words = string.split()

longest = words[0]

for i in words:
    if len(i) > len(longest):
        longest = i

print("Longest word:", longest)