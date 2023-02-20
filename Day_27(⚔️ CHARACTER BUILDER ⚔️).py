import os, time, random

def rollDice(side):
  result = random.randint(1, side)
  return result

def health():
  healthStat = ((rollDice(6)*rollDice(12))/2)+10
  return healthStat

def strength():
  strengthStat = ((rollDice(6)*rollDice(8))/2)+12
  return strengthStat

while True:
  print("⚔️ CHARACTER BUILDER ⚔️\n")
  name = input("Name your Legend: ")
  type = input("Character Type (Human, elf, Wizard, Orc: \n")
  print("HEALTH", health())
  print("STRENGHT", strength())
  print("May your name go down in Legend...\n")

  playAgain = input("Again?: \n").upper()
  if playAgain == "NO":
    break
  #else:
    #continue
  time.sleep(1)
  os.system("clear")
  
