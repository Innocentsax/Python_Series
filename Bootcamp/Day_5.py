print("==> LOVE CALCULATOR <==\n")

name1 = input("Name of the Boyfriend: ").upper()
name2 = input("Name of the Girlfriend: ").upper()

letter_T = name1.count('T') + name2.count('T')
letter_R = name1.count('R') + name2.count('R')
letter_U = name1.count('U') + name2.count('U')
letter_E1 = name1.count('E') + name2.count('E')
true_total = letter_T + letter_R + letter_U + letter_E1

letter_L = name1.count('L') + name2.count('L')
letter_O = name1.count('O') + name2.count('O')
letter_V = name1.count('V') + name2.count('V')
letter_E2 = name1.count('E') + name2.count('E')
love_total = letter_L + letter_O + letter_V + letter_E2

love_result =int(str(true_total) + str(love_total))

if love_result > 75:
  print(f"Your love score is {love_result}, You are the bone of his bone")
elif love_result >= 50 and love_result <= 74:
  print(f"Your love Score is {love_result}, and you are perfect together")
elif love_result >= 30 and love_result<= 49:
  print(f"Your love Score {love_result}, and you are compartible")
else:
  print(f"Your love Score is {love_result}, But am not sure you where meant for each other....Please pray to get confirmation from God")




print("==> TIPS CALCULATOR <==")

totalBill = int(input("Kindly enter your total bills $ "))
tips = int(input("\nWhat Percent of tips do you want to give us..10, 12 or 15: "))
spilt_bill = int(input("\nHow many people is splitting the bill: "))

tip_percent = ((tips/100) * totalBill) + totalBill
bills = round((tip_percent/spilt_bill), 2)
#bills = "%.2f" % (bills)
print(f"\nHere is the total bills ${bills} per person")



print("==> YOUR REMAINING DAYS, MONTHS AND YEARS ON EARTH <==")
print()

totalAge = int(input("Kindly enter the number of years you want to live on earth: "))
print()
current_Age = int(input("What's your age: "))
remaining_age = totalAge - current_Age

months = remaining_age * 12
weeks = remaining_age * 52
days = remaining_age * 365
print()

print(f"You have {days} days, {weeks} weeks, {months} months  and {remaining_age} left")



print("==> FIZZBUZZ GAME <==")
#RULE_1: Any number divided by 3 without a remainder = print FIZZ
#RULE_2: Any number divided by 5 without a remainder = print BUZZ
#RULE_3: Any number divided by 3 and 5 without a remainder = print FIZZBUZZ
for i in range(1, 101):
  if i % 3 == 0 and i % 5 == 0:
    print("FizzBuzz")
  elif i % 3 == 0:
    print("Fizz")
  elif i % 5 == 0:
    print("Buzz")
  else:
    print(i)


print("==> BMI CALCULATOR <==")
print()

height = float(input("Kindly enter your height in cm: "))
weight = float(input("Kindly enter your weight in kg: "))
mulHeight = height * height
BMI = round((weight/mulHeight), 2)
#print(BMI)
print()
if BMI < 18.5:
  print(f"Your BMI is {BMI}, You are Underweight")
elif BMI >= 18.5 and BMI < 25:
  print(f"Your BMI is {BMI}, You have Normal Weight")
elif BMI >= 25 and BMI < 30:
  print(f"Your BMI is {BMI}, You are slightly Overweight")
elif BMI >= 30 and BMI < 35:
  print(f"Your BMI is {BMI}, You are Obese")
elif BMI > 35:
  print(f"Your BMI is {BMI}, You are Clinically Obese")
else:
  print("INVALID BMI")
