# Here is the a TIP CALCULATOR that uses various Arithmetic Operator. 
print("==>","\033[35m","TIPS CALCULATOR","\033[0m","<==")
print()
bill = float(input("How much did you Spend: "))
percent = float(input("What percentage do you want to tip: "))
people = float(input("How many people in your group: "))
ps = (percent / 100) * bill
sum = bill + ps
div = sum / people
div = round(div, 2)
print("You each owe $", div)
