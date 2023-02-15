'''Libraries are collections of code that other people have written. Video games often use massive libraries (for example: game engines) to create the epic water reflections, 3-D graphics, etc.

print("==> RANDOM LIBRARY <==")
print()
import random

#myNumber = random.randint(1, 100)#randint is a function
for i in range(10):
  myNumber = random.randint(1, 100)
  print(myNumber)'''



print("Welcome to Guess the Number.")
print()
print("Guess a number between 1 and 1,000,000 and I will tell you if you are too low, too high, or get it correct.")
print()
print("Let's play!")

import random
attempt = 1
myNumber = random.randint(1,1000000)

while True: 
  user_guess = int(input("Pick a number between 1 and 1,000,000: "))
  if user_guess < myNumber:
    print("That number is too low. Try again!")
    attempt += 1
  elif user_guess > myNumber:
    print("That number is too high. Try again!")
    attempt += 1
    continue
  elif user_guess == myNumber:
    print("You are a winner! 🥳🥳")
    break 
    exit()
  else:
    print("That is not a number I recognize.")
print("It took you", attempt, "attempt(s) to get the correct answer.")
