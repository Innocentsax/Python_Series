def newPrint(color, word):
  if color=="red":
    print("\033[31m", word, sep="", end="")
  elif color=="green":
    print("\033[32m", word, sep="", end="")
  elif color=="blue":
    print("\033[34m", word, sep="", end="")
  else:
    print("\033[0m", word, sep="", end="")

print("Super Subroutine")
print("With my ", end="")
newPrint("red", "new program")
newPrint("reset", " I can just call red('and') ")
newPrint("red", "it will print in red ")
newPrint("blue", "or even blue")

print("That GIANT white cursor")
import os, time
#print('\033[?25l', end="") #ADD A GIANT WHITE CURSOR
print("\033[?25h", end="")# REMOVE THE CURSOR
for i in range(1, 101):
  print(i)
  time.sleep(0.3)
  os.system("clear")
print('\033[?25l', end="") #ADD A GIANT WHITE 

import os, time

for i in range(1, 101):
  print(i)
  time.sleep(0.3)
  os.system("clear")
  

print("If you put ", "\033[33m", "nothing as the ", "\033[35m", "end character ", "\033[32m", "then you don't ", "\033[0m", "get odd gaps ", sep="")

print("If you put", "\033[33m", "Nothing as the","\033[35m", "end character","\033[32m", "then you don't","\033[0m", "get odd gaps", end="")


print("COLOUR PRINTING with sep")
print("\033[35m", end="")
print("Innocent Charles Udo")
print("\33[33m", end="")
print("My name is SE UIC")
print("If you put")
print("\033[33m", end="") #yellow
print("nothing as the")
print("\033[35m", end="") #purple
print("end character")
print("\033[32m", end="") #green
print("then you don't")
print("\033[0m", end="") #default
print("get odd gaps")

for i in range (1,100):
  print(i, end="\v")
for i in range(1,100):
  print(i, end = "\t")
for i in range(0, 100):
  print(i, end = "\n")
