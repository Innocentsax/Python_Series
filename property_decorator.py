"""@PROPERTY DECORATOR -(Getter, setter and Deleter) IN PYTHON"""

class Employee:#super class
  salary_increase = 1.5

  def __init__(self, firstname, lastname, pay):
    self.firstname = firstname
    self.lastname = lastname
    self.pay = pay
    self.email = firstname + '.' + lastname + '@gmail.com'

  @property #Decorator
  def fullname(self):
    return '{} {} {}'.format(self.firstname, self.lastname, self.email)

  @fullname.setter
  def fullname(self, name):
    firstname, lastname = name.split(' ')
    self.firstname = firstname
    self.lastname = lastname

  @fullname.deleter
  def fullname(self):
    print('Deleted Name')
    self.firstname = None
    self.lastname = None
  
  @property
  def applied_salary_increase(self):
    self.pay = int(self.pay * self.salary_increase) # int, float, eval
    
  
vic = Employee("Victor", "Stephen", 15000)
vic_2 = Employee("Innocent", "Udo", 20000)

print(vic.fullname)
#print(vic_2.applied_salary_increase)
vic_2.applied_salary_increase
print(vic_2.pay)

#Here is for setter
vic.fullname = 'Gen killer'
print(vic.fullname)

#Here is for Deleter
del vic.fullname
