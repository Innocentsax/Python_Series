#Attempted
print("==> STAR WAR NAME GENERATOR")

name = input("Firstname > ").strip().capitalize()
name1 = input("Second > ").strip().capitalize()

slice = name[0:4] + " " + name1[0:4]
#slice1 = name1[0:4]
print(slice)

#Correction
print("STAR WARS NAME GENERATOR")

all = input("Enter your first name, last name, Mum's maiden name and the city you were born in ").split()

first = all[0].strip()
last = all[1].strip()
maiden = all[2].strip()
city = all[3].strip()


#Debug
name = f"{first[:3].title()}{last[:3].lower()} {maiden[:2].title()}{city[-3:].lower()}"

print(f"Your Star Wars name is {name}")


#Lesson 1
# This code should output 'Hello there'
myString = "Hello there my friend."
print(myString[0:11:1])

str = "Hello there my friend"
print(str.split())
for i in str:
   print(i)
