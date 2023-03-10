# How to navigate using Absolute path
from pathlib import Path

# Types of path in Python
# Absolute path and Relative Path

path = Path("ecommerce")
print(path.mkdir()) # mkdir makes a new directory
print(path.rmdir()) # rmdir removes the directory
print(path.glob('*.py'))
for file in path.glob('*.py'): #print all the py file in your current directory
    print(file)


print("==> Day 3 <==")
#FUNCTIONS IN PYYHON

#def min(first, second):
 # if first > second:
  #  return(second)
  #else:
   # return(first)

print(min(1, 3))

num = 20
def multiply(n):
  n = n * 10
  num = n
  print(f"value of num inside function: {num}")

multiply(num)
print(num)
print()
#the DEF function
new_list = [20, 30, 40, 50]

def sum(my_list):
  my_list[0] *=10
  my_list[1] *=10
  my_list[2] *=10
  my_list[3] *=10
  
sum(new_list)
print(new_list)
print()

#the FIND, INDEX, REPLACE, UPPER, LOWER, JOIN, FORMAT function 
txt = "Hello Innocent"
m = txt.find("l", 2, 12)
print(m)

txt = "Hello Innocent"
m = txt.index("l", 2, 12)
print(m)

str = "Innocent Charle Python"
new_str = str.replace("Python", "Udo")
print(new_str)

print("innocent Charles". upper())

print("INNOCENT CHARLES". lower())

listme = ['a', 'b', 'c']
print(" ,><".join(listme))

inno = "Learn Python {} at {}".format(3, "Bootcamp")
print(inno)

# ORD function use to check the UNICODE ASCII TABLE
print(ord('a'))
print(ord('A'))

#Lambdas function
lamb = lambda num: num * 10
print(lamb(3))

my_func = lambda num: "High" if num > 50 else "Low"
print(my_func(51))

#Functions as Argument
def add(n1, n2):
  return n1 + n2

def sub(n1, n2):
  return n1 - n2
#print(sub(2, 5))
def calc(operation, n1, n2):
  return operation(n1, n2)
print(calc(add, 2, 5))

#MAP, LIST and FILTER function
#syntax of map: map(function, list)
num_list = [0, 1, 2, 3, 4, 5]
var = map(lambda n: n*2, num_list)
print(list(var))

num_list = [100, 9, 25, -3, 41, 5]
var = filter(lambda n: n>10, num_list)
print(list(var))

#Recursion
#a process where a function calls it own self during its execution
def count(num):
  print(num)
  #put a base case
  if num == 0:
    return 0
    
  count(num -1)
                 
count(10)
print()
print()

#The fibonacci sequence is the series of numbers
#formula = X(n) = X(n-1) + X(n-2)
def fib(n):
  if n <= 1:
    return n
  else:
    return fib(n-1) + fib(n-2)

for i in range(10):
  print(fib(i))
