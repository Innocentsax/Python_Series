import os, time
print("Welcome to ALX Login page")
time.sleep(2)
print("Login Authentication")
time.sleep(2)
username = input("Kindly store your username in our database: ")
time.sleep(1)
os.system("clear")
password = input("Kindly store your password in our database: ")
time.sleep(1)
os.system("clear")
while True:
  username1 = input("Enter your user name: ")
  user_password = input("Enter your password: ")
  if username1 == username and user_password == password:
    print("\nHey!! You are welcome")
    break
  elif username1 == username and user_password != password:
    print()
    print("\033[31m","Wrong passord!!", "\033[0m")
    continue
  elif username1 != username and user_password == password:
    print()
    print("\033[31m","Wrong username!!", "\033[0m")
  else:
    print()
    print("\033[31m","Incorrect username and Password!!, Please try again", "\033[0m")
