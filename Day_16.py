print("==> Name the Lyrics game <==")
print()

count = 1
while True:
  print("Please, kindly fix the missing word")
  fix = input("I believe i can ...?")
  #count += fix
  if fix == "Fly" or fix == "fly":
    print("Amazing!! You did it")
  else:
    print("Please try again")
    count +=1
  if fix == "fly":
    break
print("Thanks for playing")

print(f"You got the correct lyrics in {count} attempt(s).")
  
print()

print("==> HOW TO CREATE YOUR LOGIN PASSWORD <==")
print()
savePassword = input("Kindly SAVE your new password: ")
print()
while True:
  pasw = input("Kindly ENTER your new password: ")
  if pasw == savePassword:
    break
  else:
    print("\033[31m","Wrong password,""\033[0m","please try again")
print("You are highly welcome")

print()

counter = 0
while True:
  ans = int(input("Enter a number: "))
  print("Adding it up")
  #counter = counter + ans
  counter += ans
  print(f"Current total is {counter}")
  addAnother = input("Add another number?: ")
  if addAnother == "no":
    break
print("Bye!")

print()



#The Boolan method of Loop
'''while True:
  print("The program is running")
  var = input("Go again?: ")
  if var == "No" or var == "no":
    break
print("Aww, I was having a good time")
print()'''
