#MODULES IN PYTHON
#class work
#import utils #First import pattern
from utils import find_max # Second import pattern

numbers = [1, 2, 3, 4, 5]  
max = find_max(numbers)
print(max)
  
# Lesson 1
import converter # just like header files in C where you store your header files and call it to ur program
from converter import kg_to_lbs # use CTRL SPACE to bring the options out.... importing specific modules
kg_to_lbs(100)

print(converter.kg_to_lbs(70))

#INHERITANCE IN PYTHON
class Mammal:
    def walk(self):
      print("walk")
      
class Dog(Mammal):
  def bark(self):
    print("Bark")

class cat(Mammal):
  def be_annoying(self):
    print("Annoying")
  

dog1 = Dog()
dog1.walk()
dog1.bark()
cat1 = cat()
cat1.be_annoying()  



#CLASS IN PYTHON
class work
class Person:
  def __init__(self, x, y): #constructive function
    self.x = x
    self.y = y
    
  def name(self):
    print("Innocent")

  def talk(self):
    print(f"Hello Class, i am {self.x}")

name = Person("Innocent", "Charles")
print(name.x)
name.talk()    

#Lesson 2 // Construct
class Point:
  def __init__(self, x, y):
    self.x = x
    self.y = y
    
  def move(self):
    print("Move")

  def draw(self):
    print("Draw")

point1 = Point(10, 20)
point1.x = 11 # You can update point1.x to 11
print(point1.x)

    

#Lesson 1
class Point:
  def move(self):
    print("Move")

  def draw(self):
    print("Draw")

#an object is an instance of a class
point1 = Point()
point1.x = 10
point1.y = 20
print(point1.x, point1.y)
point1.draw()

point2 = Point()
point2.x = 1
print(point2.x)
