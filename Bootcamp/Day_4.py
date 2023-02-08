print("==> THE RANGE FUNCTION IN PYTHON <==")
print()
#range() or list function
#range (start, end, step) e.g range(10) == range(0, 10)

for i in range(1, 11):
  if i % 2 == 0:
    print(i, "is an even number")
  else:
    print(f"{i} is an odd number")
print()

my_list = [2.5, 16.4, 10.8, 18.77, 9]
for i in range(0, 5):
  my_list[i] = my_list[i] * 2
print(my_list)
print()

#how many element that is greater than 10.
my_list = [2.5, 16.4, 10.8, 18.77, 9]
count = 0
for num in my_list:
  if num > 10:
    count = count + 1
print(count)

print()

#Nested for loop
for i in range(0, 5):
  if i == 3:
    break #the break function
  print(f"Out of the loop {i}")
  for j in range (0, 3):
    print(f"Inside the loop {j}")
print() 

for i in range(0, 5):
  if i == 3:
    continue #the continue function
  print(f"Out of the loop {i}")
  for j in range (0, 3):
    print(f"Inside the loop {j}")
print()

#The List function
my_list = list(range(0, 10))
#print(my_list)
for i in my_list:
  if i == 3 or i == 5 or i == 9:
    continue
  print(i)
print()

#The WHILE LOOP in Python
i = 0
while i < 6:
  print(i)
  if i == 3:
      break #The break function
  i += 1
  print()

i = 0
while i < 6:
  i += 1
  if i == 3:
      continue #The contiune function
  print(i)

friend = "Yes"
while friend != "Yes":
  print("Hello")
  friend = input("Do you want to be my friend?: ")
print()

#Data structure (ARRAYS) IN PYTHON
my_list = ["Innocent", "Charles", 27, 27.5]
my_list[1] = "Innocentsax"
print(my_list)

print(list(range(0, 20, 3)))
print()

world_cup_winners = [[2006, "Italy"], [2010, "Spain"], [2014, "Germany"], [2018, "France"], [2022, "Argentina"]]

world_cup_winners[4] = [2022, "MESSI😎"]
print(world_cup_winners)
print()

#METHODS IN PYTHON
#Merging list in arrays
partA = [1, 2, 3]
partB = [4, 5, 6]
merged = partA + partB
print(merged)

print()

partA = [1, 2, 3]
partB = [4, 5, 6]
partA.extend(partB)# The extend method
print(partA)

print()

apped_list = []
apped_list.append(1)#the Append Method
apped_list.append(2)
apped_list.append(3)
print(apped_list)

print()

partC = [1, 2, 3]
partC.insert(4, 5)#The insert method
partC.insert(2, 18)
print(partC)

print()

delete = [1, 2, 3, 7, 9, 8]
delete.pop(3)#The insert method
print(delete)

print()

remov = [1, 2, 3, 7, 9, 8]
remov.remove(3)#The Remove Method
print(remov)


print()

st = [1, 5, 3, 7, 2, 8]
st.sort()#The Sort Method
print(st)

print()

#The Tuple list: its a fixed list that can't be edited or modified. 
num_tuple = (1, 5, 3, 7, 2, 8)
print(num_tuple)

