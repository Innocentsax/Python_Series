import os, time
print("==> To Do List Manager <==")
ToDoListManager = []

def DisplayList():
  print()
  for items in ToDoListManager:
    print()
    print(items)

while True:
  menu = input("\nDo you want to view, add, edit, or remove an item from the to do list?: ").upper()
  if menu == "VIEW":
    DisplayList()
  elif menu == "ADD":
    items = input("\nWhat do you want to add: ")
    ToDoListManager.append(items)
  elif menu == "REMOVE":
    items = input("\nWhich item do you want to remove: ")
    check = input("\nAre you sure you want to remove this? YES or NO: ").upper()
    if check == "YES":
      if items in ToDoListManager:
        ToDoListManager.remove(items)
  elif menu == "EDIT":
    items = input("What do you want to edit: \n")
    new = input("What do yo want to change it to: \n")
    for i in range(0,len(ToDoListManager)):
      if ToDoListManager[i] == items:
        ToDoListManager[i] = new
  elif menu == "DELETE":
    ToDoListManager = []
  time.sleep(1)
  os.system("clear")
  
