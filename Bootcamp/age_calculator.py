#Age Calculator
print("==>","\033[31m","Age Calculator","\033[0m","<==")
yob = int(input("What's your year of birth: "))
mob = int(input("Month of Birth: "))
dob = int(input("Day of Birth: "))
cy = int(input("What the current year: "))
result = cy - yob
print(f"Your date of Birth is {dob}/{mob}/{yob} and ", end=" ")
print(f"You are {result} years old")
