import os, time
listOfEmail = []
def printEmail():
  print("Lists of Emails\n")
  '''for index in range(len(listOfEmail)):
    print(f"{index}: {listOfEmail[index]}")'''
  count = 1 #Add a counter
  for email in listOfEmail:
    print(f"{count}: {email}") #Make this an f-string
    count += 1 # Adds a number with each new email
  print()

def spam(max):
  for i in range(0,max):
    print(f"""Email {i+1}
  Dear {listOfEmail[i]}
It has come to our attention that you're missing out on the amazing Replit 100 days of code. We insist you do it right away. If you don't we will pass on your email address to every spammer we've ever encountered and also sign you up to the My Little Pony newsletter, because that's neat. We might just do that anyway.

Love and hugs,

Ian Spammington III""")

while True:
  print("SPAMMER Inc.")
  menu = input("1: Add email\n2: Remove email\n3: Show emails\n4: Get Spamming\nselect any number above: ")
  if menu == "1":
    email = input("Type in your email: ")
    listOfEmail.append(email)
  elif menu == "3":
    printEmail()
  elif menu == "2":
    email = input("Email > ")
    if email in listOfEmail:
      listOfEmail.remove(email)
  elif menu == "4":
    spam(10)
  time.sleep(2)
  os.system("clear")
