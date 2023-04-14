"""PYTHON INPUT AND OUTPUT"""

#Lesson 4
#Writing into a file
with open(file="mydata.txt", mode="w", encoding="utf-8") as Innocent:
  Innocent.write("Hi Everyone.\nMy name is Innocent Charles\nAm from Akwa Ibom state, but i based in Abuja\nAm passionate about programming and coding\nand my aim is to become a global software engineer")

with open(file="mydata.txt", encoding="utf-8") as Innocent:
  lineNum = 1
  while True:
    line = Innocent.readline()
    if not line:
      break
    print("line", lineNum)

    #using the split function
    wordList = line.split()

    #find the length of word in the list
    print("Number of words:", len(wordList))

    #Loop count characters in the wordList
    charCount = 0
    for word in wordList:
      for char in word:
        charCount +=1
    
    #Divide character count/length word list
    avgNumChars = charCount/len(wordList)
    print("Avg Word Length : {:.2}".format(avgNumChars))
    lineNum +=1

# Lesson 3
#Writing into a file
with open(file="mydata.txt", mode="w", encoding="utf-8") as Innocent:
  Innocent.write("Hi Everyone.\nMy name is Innocent Charles\nAm from Akwa Ibom state, but i based in Abuja\nAm passionate about programming and coding\nand my aim is to become a global software engineer")

with open(file="mydata.txt", encoding="utf-8") as Innocent:
  lineNum = 1
  while True:
    line = Innocent.readline()
    if not line:
      break
    print("line", lineNum, " : ", line, end='' )
    lineNum +=1


# lesson 2 alternative
def fib(num):
  if num == 0:
    return 0 
  elif num == 1:
    return 1
  else:
    result = fib(num - 1 + fib(num - 2))
    return result

#Ask the user the number the want
numf = int(input("Kindly input your number: "))

#Loop while calling for each number
i = 1
while i < numf:
  new = fib(i)
  print(new)
  i +=1
print("All done")
  
  
lesson 1
import os
#Writing into a file
with open(file="mydata.txt", mode="w", encoding="utf-8") as Innocent:
  Innocent.write("Hi Everyone.\nMy name is Innocent Charles\nAm from Akwa Ibom state, but i based in Abuja\nAm passionate about programming and coding\nand my aim is to become a global software engineer")
  
#Reading the contains of the file
with open(file="mydata.txt", encoding="utf-8") as Innocent:
  print(Innocent.read())

#Other files operation
print(Innocent.closed)
print(Innocent.name)
print(Innocent.mode)

#Carring out Operation with os
os.rename("mydata.txt", "file.txt")

os.remove("file.txt")
os.chdir("input")
#os.mkdir("input")
print("Current Directory:", os.getcwd())
os.chdir("..")
os.rmdir("input")
