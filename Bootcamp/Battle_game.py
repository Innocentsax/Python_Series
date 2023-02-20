import os, time, random

def rollDice(side):
  result = random.randint(1, side)
  return result

def health():
  healthStat = ((rollDice(6)*rollDice(12))/2)+10
  return healthStat

def strength():
  strengthStat = ((rollDice(6)*rollDice(8))/2)+10
  return strengthStat

print("⚔️ BATTLE TIME ⚔️\n")
c1Name = input("Name your Legend:")
c1Type = input("Character Type(Human, ELF, Wizard, Orc): \n")
print(c1Name)
c1Health = health()
c1Strength = strength()
print("HEALTH", c1Health)
print("STRENGTH", c1Strength)
print()

c2Name = input("Name your Legeng: ")
c2Type = input("Character type (Human, ELF, Wizard, Orc): ")
print()
print(c2Name)
c2Health = health()
c2Strength = strength()
print("HEALTH", c2Health)
print("STRENGTH", c2Strength)

round = 1
winner = None

while True:
  time.sleep(1)
  os.system("clear")
  print("⚔️ BATTLE TIME ⚔️")
  print()
  print("The Battle Begins")

  c1Dice = rollDice(6)
  c2Dice = rollDice(6)

  difference = abs(c1Strength - c2Strength) + 1
  if c1Dice > c2Dice:
    c2Health -= difference
    if round == 1:
      print(c1Name, "Wins the first blow")
    else:
      print(c1Name, "Wins round", round)
  elif c2Dice > c1Dice:
    c1Health -= difference
    if round==1:
      print(c2Name, "wins the first blow")
    else:
      print(c2Name, "wins round", round)
  else:
    print("Their swords clash and they draw round", round)

  print()
  print(c1Name)
  print("HEALTH:", c1Health)
  print()
  print(c2Name)
  print("HEALTH:", c2Health)
  print()

  if c1Health<=0:
    print(c1Name, "has died!")
    winner = c2Name
    break
  elif c2Health<=0:
    print(c2Name, "has died!")
    winner = c1Name
    break
  else:
    print("And they're both standing for the next round")
    round += 1
    

time.sleep(1)
os.system("clear")
print("⚔️ BATTLE TIME ⚔️")
print()
print(winner, "has won in", round, "rounds")
  
