print("Welcome to Math Facts Game")
print()
print("How well do you know your math facts? Pick a number and I will give you 10 math facts to solve.")
print()

count = 0
mul = int(input("Name of multiples: "))
for i in range (1, 11):
  solve = i*mul
  print(i,"x",mul,"=")
  ans = int(input("> "))
  if ans == solve:
    print("Amazing!! You got it right")
    count +=1
  else:
    print("That's not correct. it should have been", solve)
  if count == 10:
    print("Wow! A perfect Score! 🥳")
  else:
    print("You got", count, "out of 10 correct")
