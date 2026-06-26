# Write a program to Count vowels and consonants.

string = input("Enter a string: ")

vowels = 0
consonants = 0

for i in string:
    if i.isalpha():
        if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u' or i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U':
            vowels = vowels + 1
        else:
            consonants = consonants + 1

print("Number of vowels:", vowels)
print("Number of consonants:", consonants)