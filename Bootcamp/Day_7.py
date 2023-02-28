print("ROCK, PAPER AND SCISSORS GAME")
import random, os
def rps():
  hand = '''
  
            ___..__
    __..--""" ._ __.'
                "-..__
              '"--..__";
   ___        '--...__"";
      `-..__ '"---..._;"
            """"----'   
  
  '''
  Rock = '''
  
      .-.  _
      | | / )
      | |/ /
     _|__ /_
    / __)-' )
    \  `(.-')
     > ._>-'
    / \/
  
  
  '''
  scissor = '''
     _       ,/'
    (_).  ,/'
     _  ::
    (_)'  `\.
             `\.
  
  
  '''
  
  pick = int(input("What do yo choose? Type 0 for ROCK, 1 for PAPER or 2 for SCISSORS: \n"))
  option_list = ["Rock", "Paper", "Scissors"]
  
  if pick == 0:
    print(Rock)
    print("Computer chose: ")
    # ROCK = 0
    pc_pick = random.randint(0, 2)
    print(pc_pick)
    if pc_pick == 0:
      print(Rock)
      print("Its a draw")
    elif pc_pick == 1:
      print(hand)
      print("You loose")
    elif pc_pick == 2:
      print(scissor)
      print("You win!!")
  # HAND == PAPER == 1
  if pick == 1:
    print(hand)
    print("Computer chose: ")
    
    pc_pick = random.randint(0, 2)
    print(pc_pick)
    if pc_pick == 0:
      print(Rock)
      print("You lose")
    elif pc_pick == 1:
      print(hand)
      print("its a draw")
    elif pc_pick == 2:
      print(scissor)
      print("You win!!")
  
  if pick == 2:
    print(scissor)
    print("Computer chose: ")
    
    pc_pick = random.randint(0, 2)
    print(pc_pick)
    if pc_pick == 0:
      print(Rock)
      print("You lose")
    elif pc_pick == 1:
      print(hand)
      print("You Win")
    elif pc_pick == 2:
      print(scissor)
      print("It's a draw")

  recursion = input("\nTo replay, type 'Yes': ")
  if recursion == 'Yes':
      os.system("clear")
      rps()
      

rps()



print("RECURCIVE CALCULATOR")
import os
def calculator():
  print('''
  
            | |          | |     | |            
    ___ __ _| | ___ _   _| | __ _| |_ ___  _ __ 
   / __/ _` | |/ __| | | | |/ _` | __/ _ \| '__|
  | (_| (_| | | (__| |_| | | (_| | || (_) | |   
   \___\__,_|_|\___|\__,_|_|\__,_|\__\___/|_|   
                                               
  
''')
  print()
  
  num1 = float(input("First number: "))
  while True:
    operator = input("Use any of this operators(+, -, /, *, %): ")
    num2 = float(input("Second Number: "))
    
    if operator == "-":
      result = num1 - num2
    elif operator == "+":
      result = num1 + num2
    elif operator == "*":
      result = num1 * num2
    elif operator == "/":
      result = num1 / num2
    elif operator == "%":
      result = num1 % num2
    
    print(f"Your answer is {result}")
  
    Recursion = input(f"Type 'Yes' to continue calculating with {result}, or Type 'No' to start a new calculator: ")
    if Recursion == 'Yes':
      num1 = result
      #os.system("clear")
      continue
    else:
      os.system("clear")
      calculator()
  
calculator()
    

print("PYTHON BOOTCAMP DAY 7")
import os, time
while True:
  
  bids = {} # an empty dictionary ==> name(key): $100(value)

  name = input("What is your name: ")
  #time.sleep(1)
  price = int(input("What's your bid:$ "))
  bids[name] = price
  #time.sleep(1)
  should_continue = input("Are there any other bidders? Type 'Yes' or 'No': ")
  if should_continue == 'No':
    break
  else:
    time.sleep(1)
    os.system("clear")
    continue
  
highest_bids = 0
for bidder in bids:
  if bids[bidder] > highest_bids:
    highest_bids = bids[bidder]
    winner_name = bidder

print(f"The winner {winner_name} with a bid of ${highest_bids}")


#How to check for the highest score
Student_Score = [78, 57, 37, 58, 28, 59, 92]

highest_score = 0
for score in Student_Score: # score is the element in the list
  if score > highest_score:
    highest_score = score

print(f"The highest number in the array is {highest_score}")

#Dictionary in Python
#Dict = {key: Value}
Dict = {1:"Greek", 2: "Innocent", 3: "Charles"} #Dictionary in python
print(Dict[2])

Dict = {"Dick1": {1: "greek"}, "Dict": 2}
print(Dict["Dict1"][1])



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
    
    
    
    
    random_set = {"Education", 100, 3.16, (True, False)}
#print(len(random_set))
random_set.discard(100)# discard element from a list
random_set.remove(3.16)#also works as discard but in this case, it print error if the item is not in the list
print(random_set)


#Addition of list in a set
empty_set = set()
empty_set.add(1)
empty_set.add(2)
empty_set.update({3, 4, 5, 6, 7})
print(empty_set)
