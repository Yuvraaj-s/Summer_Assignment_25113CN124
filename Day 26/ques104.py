# Write a program to Create quiz application.

score = 0

print("Welcome to the Quiz!\n")

print("Q1. What is the capital of India?")
print("a) Mumbai")
print("b) Delhi")
print("c) Kolkata")
ans = input("Enter your answer: ")

if ans == "b" or ans == "B":
    score = score + 1

print("\nQ2. What is 2 + 2?")
print("a) 3")
print("b) 4")
print("c) 5")
ans = input("Enter your answer: ")

if ans == "b" or ans == "B":
    score = score + 1

print("\nQ3. Which language is used for AI?")
print("a) Python")
print("b) HTML")
print("c) CSS")
ans = input("Enter your answer: ")

if ans == "a" or ans == "A":
    score = score + 1

print("\nQuiz Finished!")
print("Your score is:", score, "/ 3")