import random

greeting_list = ["Bonjour: French", "Spanish: Hola", "Russian: Zdravstvuyte", "Chinese: Nǐn hǎo", "Italian: Salve", "Japanese: Konnichiwa", "German: Guten Tag"]
rnad = random.randint(0,6)
print(greeting_list[rnad])
#for greeting_list in greeting_list:
  #greeting_list = str(random.randint(0,6))
  #print(greeting_list)

grocery_list = ["bananas", "bread", "milk", "eggs", "juice", "cheese"]
print(f"The first grocery item to buy is {grocery_list[0]}.")


timetable = ["Computer Science", "Math", "English", "Art", "Sport"]
for timetable in timetable:
  print(timetable)
