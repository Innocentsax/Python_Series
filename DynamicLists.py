import os, time
toDoList = []

def printList():
  print()
  for item in toDoList:
    print(item)
    print()

while True:
  menu = input("\nToDoList Manager\n\nDo you want to view, add, or edit the ToDoList?\n").upper()
  if menu == "VIEW":
    printList()
  elif menu == "ADD":
    item = input("What do you want to add?\n")
    toDoList.append(item)
  elif menu == "EDIT":
    item = input("Do you want to remove?\n")
    if item in toDoList:
      toDoList.remove(item)
  time.sleep(5)
  os.system("clear")  



myPartyList = []
def printList():
  print() 
  for item in myPartyList:
    print(item)
  print() 

while True:
  menu = input("add or remove?: ")
  if menu == "add":
    item = input("Who should I add to the party list?: ")
    myPartyList.append(item)
  elif menu == "remove":
    item = input("Who should I remove from the party list?: ")
    if item in myPartyList:
      myPartyList.remove(item)
    else:
      print(f"{item} was not in the list")
  printList()


import os
myAgenda = []

def printList():
  print() 
  for item in myAgenda:
    print(item)
  print() 

while True:
  menu = input("add or remove?: ")
  os.system("clear")
  if menu == "add":
    item = input("What's next on the Agenda?: ")
    myAgenda.append(item)
  elif menu == "remove":
    item = input("What do you want to remove?: ")
    for item in myAgenda:
      myAgenda.remove(item)
  else:
    print(f"{item} was not found in the list")
  printList()
