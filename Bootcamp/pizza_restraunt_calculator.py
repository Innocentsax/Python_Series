print("==> PIZZA RESTRAUNT CALCULATOR <==")

size = input("What size of pizza do you want? Small, Medium and Large: ").upper()
add_pepperoni = input("Do you want pepperoni? YES OR NO: ").upper()
extra_cheese = input("Do you want extra cheese? YES OR NO: ").upper()


if size == "SMALL":
  bill = 15 #Small sized pizza price
  if add_pepperoni == "YES":
    bill += 2 # $2 is the prize for adding pepperoni
    if extra_cheese == "YES":
      bill += 1 # $ is the prize for adding extra cheese
      print(f"\nYour final bill is ${bill}")
    elif extra_cheese == "NO":
      print(f"\nYour total bill is ${bill}")
    else:
      print("Incorrect input, please try again")
  elif add_pepperoni == "NO":
    if extra_cheese == "YES":
      bill += 1
      print(f"\nYour final bill is ${bill}")
    elif extra_cheese == "NO":
      print(f"\nYour total bill is ${bill}")
    else:
      print("Incorrect input, please try again")
  else:
    print("Invalid input, Please try again")

elif size == "MEDIUM":
  bill = 20 #Medium sized pizza price
  if add_pepperoni == "YES":
    bill += 3 # $3 is the prize for adding pepperoni
    if extra_cheese == "YES":
      bill += 1 # $ is the prize for adding extra cheese
      print(f"\nYour final bill is ${bill}")
    elif extra_cheese == "NO":
      print(f"\nYour total bill is ${bill}")
    else:
      print("Incorrect input, please try again")
  elif add_pepperoni == "NO":
    if extra_cheese == "YES":
      bill += 1
      print(f"\nYour final bill is ${bill}")
    elif extra_cheese == "NO":
      print(f"\nYour total bill is ${bill}")
    else:
      print("Incorrect input, please try again")
  else:
    print("Invalid input, Please try again")

elif size == "LARGE":
  bill = 25 #Large sized pizza price
  if add_pepperoni == "YES":
    bill += 3 # $3 is the prize for adding pepperoni
    if extra_cheese == "YES":
      bill += 1 # $ is the prize for adding extra cheese
      print(f"\nYour final bill is ${bill}")
    elif extra_cheese == "NO":
      print(f"\nYour total bill is ${bill}")
    else:
      print("Incorrect input, please try again")
  elif add_pepperoni == "NO":
    if extra_cheese == "YES":
      bill += 1
      print(f"\nYour final bill is ${bill}")
    elif extra_cheese == "NO":
      print(f"\nYour total bill is ${bill}")
    else:
      print("Incorrect input, please try again")
  else:
    print("Invalid input, Please try again")
else:
  print("\n input, please try again")
