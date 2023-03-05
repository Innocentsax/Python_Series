"""LIST IN PYTHON"""
# 2D List in Python
matrix = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]
print(matrix[0][0])


#Write a program to find the largest number in a list
num = [2, 4, 9, 18, 16]
max = num[0]
for number in num:
  if number > max:
    max = number
print(max)


"""NESTED FOR LOOP IN PYTHON"""
number = [2, 2, 2, 2, 6]
for x_count in number:
  #print("x" * x_count)#Here is the easy way to print F
  output = ''
  for count in range(x_count):
    output += 'x'
  print(output)
#Lesson1
for x in range(4):
  for y in range(3):
    print(f"{x}:{y}")

"""FOR LOOP IN PYTHON"""
for item in "Python": #loop through a string
  print(item)

for item in ['Innocent', 'Charles', 'Udo']:#iterate/loop through the list
  print(item)

prices = [10, 20, 30, 40]
total = 0
for price in prices:
  total += price
print(total)
