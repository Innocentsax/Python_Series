print("==> THE USE OF F-STRINGS <==\n")

for i in range(1,30):
  statement = input(f"What's your thought about the {i} days of code: ")
  print()

  myText = f"You thought Day {i} was"
  print(f"{myText:^35}")
  $print(f"{statement:^35}")
  print()

  #print(f"Your thought for Day {i:^40} is {statement}")

food = "pizza"
location = "beach"
color = "green"
friend = "Quinn"

response = "Alejandra ordered {food} to eat at the {location} with her friend, {friend}. She got to the {location} and looked for a {color} umbrella where {friend} said they would be waiting. By the time, Sally found {friend}, the {food} was cold and the {location} was lame.".format(food=food, location=location, friend= friend, color=color,)

print(response)


for i in range(1,31):
  print(f"Day {i: >10} out of 31")

  
name = "Katie"
age = "28"
pronouns = "she/her"

response = f"This is {name}, using {pronouns} pronouns, and is {age} years old. Hello, {name}. How are you? Have you been having a great {age} years so far"

print(response)



name = "Katie"
age = "28"
pronouns = "she/her"

response = "This is {name}, using {pronouns} pronouns, and is {age} years old. Hello, {name}. How are you? Have you been having a great {age} years so far".format(name=name, pronouns=pronouns, age=age)

print(response)


name = "Katie"
age = "28"
pronouns = "she/her"

print("This is {name}, using {pronouns} pronouns, and is {age} years old. Hello, {name}. How are you? Have you been having a great {age} years so far".format(name=name, pronouns=pronouns, age=age))


name = "Innocent Charles"
age = "26"
occupation = "Software Engineer"

print("My name is {}, and {} years old. am a {} at Google.".format(name, age, occupation))
