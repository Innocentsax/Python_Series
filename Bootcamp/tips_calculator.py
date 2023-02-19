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
