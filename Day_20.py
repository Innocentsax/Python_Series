print("==> MULTIPLICATION TIMES-TABLE <==")
print()

multiple = int(input("Kindly input the times-table number you want: "))
for i in range (1, 13):
  print(i, "x", multiple, "=", i*multiple)




'''List Generator
Ask the user to list a starting number, ending number, and increment to use. Display an answer based on the users' answers (use the input command.)'''

start = int(input("Kindly enter your start number: "))
end = int(input("Kindly enter your endline number: "))
incre = int(input("kindly input the level of increment: "))
for i in range (start, end, incre):
  print(i)


  
for i in range(10, 0, -1):
  print(i)
for i in range (0, 100000, 25):
  print(i)

for i in range(1,13):
  print(f"{i} x 13 = ", i*13)
