print("==> Loan Calculator <==")
loan = 1000
apr = 0.05
for i in range(10):
  loan +=(loan*apr)
  print(f"Year {i+1} is {round(loan,2)}")

'''total = 10
for counter in range (100):
  total += 10
  print("total", counter)
  
total = 0
for num in range (100):
  total += num
  print(total)


#THE CONCEPT OF WHILE LOOP IN PYTHON
counter = 0
while counter < 10:
  print(counter)
  counter +=2
print()

#THE CONCEPT OF FOR LOOP IN PYTHON
for count in range(0, 10, 2):
  print(count)'''
