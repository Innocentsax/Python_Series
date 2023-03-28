#task 4 wuth Dere Banas: if Statment
age = eval(input("Enter your Age: "))
if age >= 1 and age <= 18:
  print("Important Birthday")
elif age == 21 or age == 50:
  print("Important Birthday")
elif not(age < 65):
  print("Important Birthday")
else:
  print("Not important")

#task 3 wuth Dere Banas: Building Calculator
# Store the user input of 2 number and the operator
num1, operator, num2 = input('Enter calculation: ').split()

#convert the strings into integers
num1 = int(num1)
num2 = int(num2)

#if Statement for the operators
if operator == "+":
  print("{} + {} = {}".format(num1, num2, num1 + num2))
elif operator == "-":
  print("{} + {} = {}".format(num1, num2, num1 - num2))
elif operator == "/":
  print("{} + {} = {}".format(num1, num2, num1 / num2))
elif operator == "%":
  print("{} + {} = {}".format(num1, num2, num1 % num2))
else:
  print("Incorret Value")


#Project_test2 with Derek Banas
"""Problem: Receive miles and convert to kilometer
kilometer = miles * 1.60934
Enter miles 5
5 miles equals 8.04 kilometer"""
mile = int(input("Enter miles > "))
result = (mile * 1.60934)
print("{} miles is = {}".format(mile, result))

#Project_test1 with Derek Banas
#Ask the user to input 2 values and store them in variables num1, num2
#Concert the strings into regular numbers interger
num1 = (input("> "))
num2 = (input("> "))

#Add the value entered
sum = num1 + num2

#Subtract values and store in sub
sub = num1 - num2

#Divide values and store in diff
dif = num1 / num2

#Multiply the values and store in product
pro = num1 * num2

#Divide the values and store in quotient
quo = num1 % num2

print(f"{sum}: {sub}: {dif}: {pro}: {quo}")
