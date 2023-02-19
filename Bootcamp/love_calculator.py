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
