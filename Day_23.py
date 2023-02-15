'''What if I told you there was a way to use code or call it and use it anytime anywhere??

That is a subroutine!!

A subroutine tells the computer that a piece of code exists and to go run that code again and again...

Subroutines work like a recipe in a cookbook. If you want to know how to make a cake, you don't have to start from scratch every time. You can use a recipe to get the same quality each time.

Just like a recipe
Subroutines work like a recipe in a cookbook. If you want to know how to make a cake, you don't have to start from scratch every time. You can use a recipe to get the same quality each time.

How do we define a subroutine?
A subroutine is defined by:

def (which stands for definition)
You need to give the subroutine a name (and just like with a variable, you can't have spaces).

You need to add () even if there are no arguments followed by a colon :. The code needs to be indented.'''

#def rollDice():
  #import random
  #dice = random.randint(1, 6)
  #print(f"You rolled {dice}")

#for i in range(10):
#  rollDice()

print("==> REPLIT LOGIN SYSTEM <==")
print()

def replitLoginSystem():
  savn = input("save Your username: ")
  savpa = int(input("Save your password: "))
  print()

  while True:
    name = input("What is your Username: ")
    password = int(input("What is your Password: "))
    if name == savn and password == savpa:
      print("Welcome to Replit")
      break
    else:
      print("Whoops! I don't recognize that username or password....Please try again")
      continue

replitLoginSystem()
