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
