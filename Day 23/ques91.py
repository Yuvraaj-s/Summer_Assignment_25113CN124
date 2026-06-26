# Write a program to Check anagram strings. 

string1 = input("Enter first string: ")
string2 = input("Enter second string: ")

if sorted(string1) == sorted(string2):
    print("Strings are anagrams")
else:
    print("Strings are not anagrams")