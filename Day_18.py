print("==> Guess the number Game <==")
print()

#This is the win number
winNum = 500000
count = 1
while True:
  guessNum = int(input("Kindly input a number from 1 to 1000000: "))

  if guessNum < 0:
    exit()
  elif guessNum < winNum:
    #continue
    print("Too low")
    count +=1
  elif guessNum > winNum:
    print("Too high")
    count +=1
    continue
  elif guessNum == winNum:
    print("You win!!")
    break
print(f"You win at {count} number of count ")


'''print("Welcome to Guess the Number.")
print()
print("Guess a number between 1 and 1,000,000 and I will tell you if you are too low, too high, or get it correct.")
print()
print("Let's play!")

correct_number = 2300
attempt = 1

while True:
  user_guess = int(input("Pick a number between 1 and 1,000,000: "))
  if user_guess < 0:
    print("Now we'll never know what the answer is …")
    exit()
  if user_guess < correct_number:
    print("That number is too low. Try again!")
    attempt += 1
  elif user_guess > correct_number:
    print("That number is too high. Try again!")
    attempt += 1
    continue
  elif user_guess == correct_number:
    print("You are a winner! 🥳🥳")
    break 
  else:
    print("That is not a number I recognize.")
print("It took you", attempt, "attempt(s) to get the correct answer.")'''
