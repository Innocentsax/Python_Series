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
