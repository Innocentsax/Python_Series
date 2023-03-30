# Class Attribute in Python

class Person:
  number_of_people = 0
  GARVITY = -9.8

  def __init__(self, name):
    self.name = name
    #Person.number_of_people += 1
    Person.add_person()

  # ClassMethod in Python
  @classmethod
  def number_of_people(cls):
    return cls.number_of_people

  @classmethod
  def add_person(cls):
    cls.number_of_people += 1
    

p1 = Person("Tim")
print(Person.number_of_people())
#print(Person.number_of_people)
p2 = Person("Jill")
print(Person.number_of_people)
Person.number_of_people = 8
print(p2.number_of_people)
Person.number_of_people = 91
print(p1.number_of_people)

# Inheritance in Python
class Pet:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def show(self):
    print(f"I am {self.name} and i am {self.age} year old")
    
class Cat(Pet):
  def __init__(self, name, age, color):
    super().__init__(name, age)
    self.color = color

  def show(self):
    print(f"i am {self.name}, {self.age} and {self.color}")
    
  def speak(self):
    print("meow")

class Dog(Pet):
  def speak(self):
    print("Bark")

# instance of the Pet Class
p = Pet("Tim", 34)
p.show()
c = Cat("Tiwiwi", 67, "blue")
c.show()
d = Dog("Dilian", 32)
d.show()

# Instance of the Cat and Dog
c = Cat("Tiwiwi", 67, "Brown")
c.speak()
d = Dog("Dilian", 32)
d.speak()

Repeated class model... convert it to a single model call inheritance
class Cat:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def speak(self):
    print("Meow")

class Dog:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def speak(self):
    print("Bark")

Basics of Classes
class Student:
  def __init__(self, name, age, grade):
    self.name = name
    self.age = age
    self.grade = grade # 1 = 100

  def get_grade(self):
    return self.grade

class Course:
  def __init__(self, name, max_students):
    self.name = name
    self.max_students =  max_students
    #self.students = []
    #self.is_active = False

  def add_student(self, student):
    self.student = []
    if len(self.student) < self.max_students:
      self.student.append(student)
      return True
    return False

  def get_average_grade(self):
    value = 0
    for student in self.student:
      value += student.get_grade()

    return value / len(self.student)

s1 = Student("Tim", 19, 95)
s2 = Student("Bill", 78, 69)
s3 = Student("Udo", 14, 45)

course = Course("Science", 2)
course.add_student(s1)
course.add_student(s2)
print(course.add_student(s3))
print(course.get_average_grade())
#print(course.student[0].name)


#LESSON 2
class Dog():
  def __init__(self, name, age):
    self.name = name #This is the attribute of a class
    self.age = age

  def get_name(self):
    return self.name

  def get_age(self):
    return self.age

  #inserting name or age attribut
  def set_new_age(self, name, age):
     self.name = name 
     self.age = age

    
d = Dog("Timi", 34)
d.set_new_age("Bill", 24)
print(d.get_name(), d.get_age())




#LESSON 1
class Dog():
  def __init__(self, name, age):
    self.name = name #This is the attribute of a class
    self.age = age
    #print(name, age)
    
  def add_one(self, x):
    return x + 1
    
  def bark(self):
    print("bark")

d = Dog("Innocent", 26) #Here is the instance of a class
print(d.name, d.age)
d2 = Dog("Bill", 78)
print(d2.name, d2.age)


#Built-in classes using the type function
class Dog():
  def add_one(self, x):
    return x + 1
    
  def bark(self):
    print("bark")

d = Dog()
print(d.add_one(5))
d.bark()
print(type(d))

def hello():
  print("hello")

print(type(hello)) # function class
x = 1
print(type(x)) # int class
print(type("Hello")) # String class


# Lesson....check again
import turtle

class Polygon:
    def __init__(self, sides, name):
        self.sides = sides
        self.name = name
        #Using Polygon table
        self.interior_angles = (self.sides-2)*180
        self.angle = self.interior_angles/self.sides

    def draw(self):
        for i in range(self.sides):
            turtle.forward(100)
            turtle.right(180-self.angle)
        turtle.done()

square = Polygon(4, "Square")
pentagon = Polygon(5, "Pentagon")

print(square.sides)
print(square.name)
print(square.interior_angles)
print(square.angle)

print(pentagon.sides)
print(pentagon.name)
#checkout KITE for documentation

#square.draw()
#pentagon.draw()
hexagon = Polygon(6, "Hexagon")
hexagon.draw()
