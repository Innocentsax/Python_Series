import random
print("==> NUMBER GUESSING GAME <==")


#win_number = 500
#count = 1
#guess_number = int(input("Kindly pick a random number from 1 to 100: "))
def set_difficulty():
    level = input("Choose a difficulty. Type 'EASY' or 'HARD': ").lower()
    if level == "easy":
        return 10 #reture 10 chances
    else:
        return 5

def check_answer(guess, answer, turns):
    if guess_number > answer:
      print("Too high, Please try again")
      return turns -1
    elif guess_number < answer:
      print("Too low, Please try again")
      return turns -1
    else:
      print(f"\nYou got it...the answer is {answer}")

answer = random.randint(1, 100)
turns = set_difficulty()

guess_number = 0
while guess_number != answer:
    guess_number = int(input("Kindly pick a random number from 1 to 100: "))
    turns = check_answer(guess_number, answer, turns)
    print(f"\nYou have {turns} attempts remainings to guess the number \n")
    if turns == 0:
      print("\nYou are out of attempt")
      break
    print(f"\nYou have {turns} attempts remainings to guess the number \n")

    
    
    
    #Random number 2
    import random


class Dice:
    def roll(self):
        first = random.randint(1, 6)
        second = random.randint(1, 6)
        return first, second


dice = Dice()
print(dice.roll())
