print("THE CONCEPT OF DEF FUNCTION")
import random

def rollDice(sides):
  result = random.randint(1,sides)
  return result

def roll_6_and_8():
  roll_6_sided_dice = rollDice(6)
  roll_8_sided_dice = rollDice(8)
  health = roll_6_sided_dice * roll_8_sided_dice
  return health

print("⚔️Character stats generator⚔️")
  

haveACharacter = "yes"

while haveACharacter == "yes":
  character = input("Name your warrior: ")
  health = str(roll_6_and_8())
  print("Their health is ", health,"hp" ) 
  haveACharacter = input("Want to create another character?")




def area_square(side1, side2):
  area = side1 * side2
  return area

area = area_square(4, 12)
print(area)


def areaOfTriangle(base, height):
  area = 0.5 * base * height
  return area

var = areaOfTriangle(5, 22)
print(var)



print("==> RANDOM PIN NUMBER GENERATOR <==")
print()
def pinPicker(number):
  import random
  pin = ""
  for i in range (number):
    pin += str(random.randint(0, 9))
  return pin

myPin = pinPicker(7)
print(myPin)
