import os
def calculator():
  print('''
  
            | |          | |     | |            
    ___ __ _| | ___ _   _| | __ _| |_ ___  _ __ 
   / __/ _` | |/ __| | | | |/ _` | __/ _ \| '__|
  | (_| (_| | | (__| |_| | | (_| | || (_) | |   
   \___\__,_|_|\___|\__,_|_|\__,_|\__\___/|_|   
                                               
  
  ''')
  print()
  
  num1 = float(input("First number: "))
  while True:
    operator = input("Use any of this operators(+, -, /, *, %): ")
    num2 = float(input("Second Number: "))
    
    if operator == "-":
      result = num1 - num2
    elif operator == "+":
      result = num1 + num2
    elif operator == "*":
      result = num1 * num2
    elif operator == "/":
      result = num1 / num2
    elif operator == "%":
      result = num1 % num2
    
    print(f"Your answer is {result}")
  
    Recursion = input(f"Type 'Yes' to continue calculating with {result}, or Type 'No' to start a new calculator: ")
    if Recursion == 'Yes':
      num1 = result
      #os.system("clear")
      continue
    else:
      os.system("clear")
      calculator()
  
calculator()
