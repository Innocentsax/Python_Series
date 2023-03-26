"""David's Nan's Bingo Card Generator"""
import random

bingo = []

def ran():
  number = random.randint(1,90)
  return number

def prettyPrint():
  for row in bingo:
    print(row)

numbers = []
for i in range(8):
  numbers.append(ran())

numbers.sort()

bingo = [ [numbers[0], numbers[1], numbers[2]], [numbers[3], "BINGO", numbers[4]], [numbers[5], numbers[6], numbers[7]] ]

prettyPrint()
#Lesson
my2Dlist = [ ["Innocent", 26, "PC"], ["Charles", 50, "Tablet"], ["Udo", 80, "Died"] ]

print(my2Dlist[0][2])
my2Dlist[0][2] = "Mac"
print(my2Dlist[0][2])
for i, a, u in my2Dlist:
  print(f"{i}: {a}: {u}")
