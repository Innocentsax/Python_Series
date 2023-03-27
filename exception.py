#Class Work
"""1. Create a file named mydata2.txt
2. Use what your learned in part 8 to find out how to open a file without with(Open in try
3. Catch FileNotFoundError
4. In else print contents
5. In finally
6. Open non-existent file mydata3.txt"""

try:
  myFile = open("mydata2.txt", encoding="utf-8")

except FileNotFoundError as ex:
  print("That file was not found")

  print(ex.args)

else:
  print("File  :", myFile.read())
  myFile.close()

finally:
  print("Finished Working with File")

  
#Lesson_3
num1, num2 = input("Enter 2 values to divide: ").split()

try:
  quotient = int(num1) / int(num2)

  print("{} / {} = {}".format(num1, num2, quotient))
  #print(f"{num1} / {num2} = {quotient}")

except ZeroDivisionError:
  print("You can't divide by Zero")

else:
  print("You didn't raise an exception")

finally:
  print("I execute no matter what")

Lesson_2
class UdoNameError(Exception):
  def __init__(self, *args, **kwargs):
    Exception.__init__(self, *args, **kwargs)

try:
  UdoName = input("What is your dogs name: ")

  if any(char.isdigit() for char in UdoName):
    raise UdoNameError
      #raise (any builtin error)

except UdoNameError:
  print("You Udo's name can't contain number")



#Lesson_ 1
try:
  list = [1,2,3]
  print(list[3])

except IndexError:
  print("Sorry this value does'nt exist")

except:
  print("Unknow value")
