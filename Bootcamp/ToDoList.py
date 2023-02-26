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
