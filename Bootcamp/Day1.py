'''This is Python bootcamp''' #Muliply line comment
print("==> PYTHON BOOTCAMP <==")

print("Inno" + "cent")
print("Innocent")
print(20 + 30)
print("Hello", end=" ")
print("World")
print(complex(3,4)) # Complex numbers for Machine Learning
var = "Hello World"
count = len(var)# string len, counts the number of alphabet in
print(count)# the variable var
m = var[0:9:1]# check a letter in a pecific location // string slicing
print(m)
print()

# Print out the identity of variables
inno = "Hello" #Same variable "inno" but the possess different ID
print(id(inno))
inno = "World"
print(id(inno))
print()
print()

# How to check the data type of variable declared
dataType = 3 + 5.8
print(type(dataType))

# adding an int to a typecasted string by type casting it with an integer datatype
x = 10 + int("10")
print(x)
print()
# How to use th format specifier sign
me = "I love %s %d" % ("Python", 3)
print(me)

print(2 > 1)
print()
print()
# Write a program that takes two number as input and print their sum, difference, product, quotient and the sum of square of the two number
num1 = float(input("Kindly enter you first number: "))
num2 = float(input("Kindly enter you second number: "))
print()
print(num1 + num2, num1 / num2, num1 * num2, num1 - num2, num1**2 + num2**2)
