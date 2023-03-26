website = {"name": None, "url": None, "desc": None, "rating": None}

for name in website.keys():
  website[name] = input(f"{name}: ")

print()
for name, value in website.items():
  print(f"{name}: {value}")
  
#Lesson1
myDick = {"name":"Innocent", "Health": "100%", #"Strength": "100%", "equipped":"God"}
for i in myDick:
  print(myDick[i])


#using the value function
for value in myDick.values():
  print(value)


#Using the Items function
for name, value in myDick.items():
  print(f"{name}: {value}")
  if (name=="Strength"):
    if value>"100%":
      print("Whoa, so Strong")
    else:
      print("Weak sauce dude ")


myDictionary = {"name" : "David the Mildy Terrifying", "health": 186, "strength": 4, "equipped":"l33t haxx0r p0werz"}

#Bugs
for name, value in myDictionary.items():
  print(f"{name}:{value}")

  if (name == "strength"):
    if value > 100:
      print("Whoa, SO STRONG")
    else:
      print("Looks like you skipped leg day, arm day, chest day and, well, gym day entirely bro!")
