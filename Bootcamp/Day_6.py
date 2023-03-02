# FUNCTIONS IN PYTHON
def callname(name, yob, curyr):
  
  dob = curyr - yob
  print(f"Your name is {name}, and you are {dob} years old\n\n")

callname("Innocent", 1996, 2023)# Order 1: Positional argument
callname(curyr=2023, name="Innocent", yob=1996)# Order 2: Scattered argument but using key word
callname("Charles", 1999, 2023)
callname("udo", 1987, 2023)

print("==> BMI CALCULATOR (M = height, kg = weight <==")

def bmi_cal(weight, height):
  bmi = weight // (height ** 2)
  print(f"Your BMI is {bmi}")

user_weg = float(input("kindly enter your weight: "))
user_heg = float(input("Kindly enter your weight: "))
bmi_cal(user_weg, user_heg)

# How to use the return Statement
def bmi_cal(weight, height):
  bmi = weight // (height ** 2)
  return bmi

bb_bmi = bmi_cal(70, 1.76)
aa_bmi = bmi_cal(65, 1.72)

if bb_bmi > aa_bmi:
  print("BB is heavier than AA")
else:
  print("AA is heavier than BB")
  
#How to use the return Statement 2
def bmi_cal(weight, height):
  bmi = weight // (height ** 2)
  weight_cm = weight * 100 #BMI weight in cm
  return (bmi, weight_cm) #returning too variable: You can either return it into  a TUPLE, LIST, DICTIONARIES AND SET i.e collection of data

bb_bmi, weight_in_cm = bmi_cal(70, 1.76)  
print(bb_bmi)
print(weight_in_cm)


#How to use the return statement 3 with other paramenter
def greeting(fname, lname, title="Mr/Mrs", mname=None):
  if mname is not None:
    str_to_return = f"Hi {title}, Your full name is {fname} {mname} {lname}"
  else:
    str_to_return = f"Hi {title}, Your full name is {fname} {lname}"
  return str_to_return

Inno = greeting(fname="Innocent",lname="Udo", title="Mr")
print(Inno)


def greet_user(*args): # TUPLE: each time you add * to you parameter, it turn it to a tuple.
  print(f"Hi {args}")

greet_user("Innocent", "Charles", "Udo")

#DICTIONARIES: **kwargs convert it to Dictionary
def greet_user(**kwargs):
  for key in kwargs:
    #print(kwargs[key])
    print(f"{key} = {kwargs[key]}")

{"fnname" : "Innocent", "lname" : "Udo"}
greet_user(fname="Innocent", lname="Charles", num=99)


# Personal lesson on Set
"""SET: Set is a collection of unique Data. i.e the element can't be duplicated.

features: a. non-indexables
         b. not ordered
         c. heterogenous and immutable
         
Operations: Union()
            intersection() 
            difference()
            symmetric difference()

"""
neu = {3, 5, 6}
myset = {3, 2,3, 5, 6}
#myset.union(myset)
#myset.intersection(neu)
#myset & neu
#myset.difference(neu)
#myset - neu
#myset.symmetric_difference(neu)
myset ^ neu
print(myset)

# Personal Lesson on Dictionary
"""Dictionaries: A collection of key-value pairs separated by commas
      CHECK: Check up the methods in Dictionaries"""
mdict = {"Math":78, "Sci": 96}
#print(mdict["Sci"])
# for m in mdict:
#   print(mdict[m])

# for subject in mdict.items():
#   print(subject)

# for subject in mdict.values():
#   print(subject)

for subject, score in mdict.items():
  print(f"Subject: {subject} and Score: {score}")

md = {"a":45, "b":46}
md["c"] = 69
print(md)

#Personal Lessons on TUPLE
"""TUPLE ( A collection of data that are immutable)
feature: Heterogeous, order, indexeable.

Declaration of Tuples:

score = 80, 75, 56, 20  #multiple tuple
score = (80, 75, 56, 20) #muliple tuple
score = 95,   #single tuple
score = (95,) #single tuple
"""
#scores = 80, 75, 56, 20
# for score in scores:
#   for i in range(len(scores)):
#     print(f"{i} : {score}")

#Swapping 2 number:
a = 10
b = 20
print(f"a: {a} and b: {b}")
# swapping the values of a snd b. let a = 20 and a = 10

temp = a  #temp = 10
a = b     # a = 20
b = temp  # b = 10
print(f"a: {a} and b: {b}")

# Using tuples to swap the number
#a, b = b, a
#print(f"a: {a} and b: {b}")
a, b == b, a
print(f"a: {a} and b: {b}")




import random
print("==> NUMBER GUESSING GAME <==")


#win_number = 500
#count = 1
#guess_number = int(input("Kindly pick a random number from 1 to 100: "))
def set_difficulty():
    level = input("Choose a difficulty. Type 'EASY' or 'HARD': ").lower()
    if level == "easy":
        return 10 #reture 10 chances
    else:
        return 5

def check_answer(guess, answer, turns):
    if guess_number > answer:
      print("Too high, Please try again")
      return turns -1
    elif guess_number < answer:
      print("Too low, Please try again")
      return turns -1
    else:
      print(f"\nYou got it...the answer is {answer}")

answer = random.randint(1, 100)
turns = set_difficulty()

guess_number = 0
while guess_number != answer:
    guess_number = int(input("Kindly pick a random number from 1 to 100: "))
    turns = check_answer(guess_number, answer, turns)
    print(f"\nYou have {turns} attempts remainings to guess the number \n")
    if turns == 0:
      print("\nYou are out of attempt")
      break
    print(f"\nYou have {turns} attempts remainings to guess the number \n")





print("==> PASSWORD GENERATOR <==")

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+', '@']

random.shuffle(letters)
random.shuffle(numbers)
random.shuffle(symbols)

user_letter = int(input("How many letters would you like in your password? "))
user_numbers = int(input("\nHow many numbers would you like? "))
user_symbols = int(input("\nHow many symbols would you like? "))

password_letters = ""
for letter in range(0, user_letter):
  password_letters = password_letters + letters[letter]
#print(password_letters)

password_numbers = ""
for number in range(0, user_numbers):
  password_numbers += numbers[number]
#print(password_numbers)

password_symbols = ""
for symbol in range(0, user_symbols):
  password_symbols += symbols[symbol]
#print(password_symbols)

derived_password = password_letters + password_numbers + password_symbols
strings_to_list = list(derived_password)
random.shuffle(strings_to_list)
lenght_of_password = len(strings_to_list)

rand_strings = ""
for list in range(0, lenght_of_password):
  rand_strings += strings_to_list[list]
print(f"\nYour new generated password is {rand_strings}, and the lenght of the password is {lenght_of_password}")
  


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


import random
#module 1
#me = random.randint(1, 15)

#module 2
list = ['a', 'b', 'c', 'd', 'e']
me = random.choice(list)
#module 3
#random.shuffle(list)
print(me)
