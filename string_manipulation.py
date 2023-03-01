"""STRING MANIPULATION"""
#MY_SOLUTION
name_list = []
def printlist():
  print()
  for items in name_list:
    for i in range(len(name_list)):
      print(f"{i} : {items}")
while True:
  firstname = input("First-name > ").strip().capitalize()
  lastname = input("Last-name > ").strip().capitalize()
  
  tidied = firstname + " " + lastname
  #print(tidied)
  item = input("Do you want to add your name to the list? Yes / No > ").strip().lower()
  if item == "yes":
    if tidied not in name_list:
      name_list.append(tidied)
      printlist()
    else:
      print("ERROR: Duplicate name")
      

#CORRECTION
rolodex = []

def printList():
  print()
  for name in rolodex:
    print(name)
  print()

while True:
  firstName = input("First Name: ").strip().capitalize()
  lastName = input("Last Name: ").strip().capitalize()
  name = f"{firstName} {lastName}"
  if name not in rolodex:
    rolodex.append(name)
  else:
    print("ERROR: Duplicate name")
  printList()



#DEBUD
whatToEat = input("What do you fancy for dinner? ")
if whatToEat.strip().lower() == "pasta": 
  print("Get out the pasta maker.")
elif whatToEat.strip().lower() == "TACOS":
  print("Let's do Taco Tuesday!")
else: 
  print("Go search the fridge.")

#LESSON2
myList = []
 
def printList():
 print()
 for i in myList:
   print(i)
 print()
 
while True:
 addItem = input("Item > ").capitalize().strip()
 if addItem not in myList:
   myList.append(addItem)
 printList()

#LESSON1

def printList():
  print()
  for items in myList:
    print(items)
    print()
while True:
  add_item = input("Item > ").capitalize().strip()
  if add_item not in myList:
    myList.append(add_item)

  printList()


name = input("What's your name: ")
if name.lower().strip() == "david":
  print("Hello Innocent")
else:
  print("What a beautiful head of hair")
