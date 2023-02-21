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
