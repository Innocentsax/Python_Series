def whichcakes(ingredient, base, coating):
  if ingredient == "Chocolate" or ingredient == "chocolate":
    print("Mhmm..Chocolate cake is amazing")
  elif ingredient == "Brocoli" or ingredient == "brocoli":
    print("You what mate")
  else:
    print("Yeah, that's great I suppose..")
  print(f"So you want a {ingredient} cake, on a {base} base, with {coating} on top ")

uringre = input("What's your cake ingredient: ")
urbase = input("What base do you want for your cake: ")
urcoating = input("what's your expected coating: ")
whichcakes(uringre, urbase, urcoating)

print()
print()
def biggerNumber(num1, num2):
  if num1 > num2:
    print(f"{num1} is bigger")
  else:
    #print(num2)
    print(f"{num2} is bigger.")

first = int(input("Enter your first number: "))
second = int(input("Enter your second number: "))
biggerNumber(first, second)

print()
print()
def pizza_order(topping1, topping2):
  if topping1 == "pepperoni":
    print(topping1, "is a great choice")
  else:
    print(topping1, "is kinda lame on pizza")
  print(topping2, "sounds delicious, much better than", topping1)
  
topping1 =  input("Name a pizza topping. ")
topping2 = input("Name a second pizza topping. ")

pizza_order(topping1, topping2)

print()
print()
import random
print("Infinity Dice 🎲")
  
sides = int(input("How many sides?: "))
playGame = "yes"
  
def rollDice(sides):
  print("You rolled ", random.randint(1,sides))
while playGame == "yes":
    rollDice(sides)
    playGame = input("Roll again?")  
