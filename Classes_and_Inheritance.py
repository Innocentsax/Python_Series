"""INHERITANCES IN PYTHON"""
class Employee:
  increase_amount = 1.5

  def __init__(self, first, last, pay):
    self.first = first
    self.last = last
    self.pay = pay
    self.email = first + '.' + last + '@email.com'

  def fullname(self):
    return '{} {}'.format(self.first, self.last)

  def apply_increase_amount(self):
     self.pay = int(self.pay * self.increase_amount)

class Developer(Employee):
  increase_amount = 5

  def __init__(self, first, last, pay, prog_lang):
    super().__init__(first, last, pay)# first Pattern
    #Employee.__init__(self, first, last, pay) //second pattern
    self.prog_lang = prog_lang

class Managers(Employee):
  
  def __init__(self, first, last, pay, employees=None):
    super().__init__(first, last, pay)
    if employees is None:
      self.employees = []
    else:
      self.employees = employees

  def add_emp(self, emp):
    if emp not in self.employees:
      self.employees.append(emp)

  def remove_emp(self, emp):
    if emp in self.employees:
      self.employees.remove(emp)

  def print_emps(self):
    for emp in self.employees:
      print('-->', emp.fullname())


dev_1 = Developer('Innocent', 'Charles', 50000, 'Python')
dev_2 = Developer('Benjamin', 'Ben', 20000, 'Java')

mgr_1 = Managers('Ibrahim', 'Sunday', 9000, [dev_1])
print(mgr_1.first, mgr_1.last, mgr_1.pay, mgr_1.employees)

mgr_1.add_emp(dev_2)
mgr_1.remove_emp(dev_1)

mgr_1.print_emps()
print()

# Builtin function "isinstance" & "issubclass"
print(isinstance(mgr_1, Managers))
print(isinstance(mgr_1, Developer))
print(isinstance(mgr_1, Employee))
print()

print(issubclass(Developer, Managers))
print(issubclass(Developer, Employee))


#Lesson 2
class Employee:
  increase_amount = 1.5

  def __init__(self, first, last, pay):
    self.first = first
    self.last = last
    self.pay = pay
    self.email = first + '.' + last + '@email.com'

  def fullname(self):
    return '{} {}'.format(self.first, self.last)

  def apply_increase_amount(self):
     self.pay = int(self.pay * self.increase_amount)

class Developer(Employee):
  increase_amount = 5

  def __init__(self, first, last, pay, prog_lang):
    super().__init__(first, last, pay)# first Pattern
    #Employee.__init__(self, first, last, pay) //second pattern
    self.prog_lang = prog_lang

class Managers(Employee):
  increase_amount = 10
  def __init__(self, first, last, pay, unit):
    Employee.__init__(self, first, last, pay)
    self.unit = unit
    
# For Manager
dev_1 = Managers('Innocent', 'Charles', 50000, 'IT')
dev_2 = Managers('Benjamin', 'Ben', 20000, 'Logistics')

print(dev_1.first, dev_1.last, dev_1.pay, dev_1.unit)
print(dev_2.first, dev_2.last, dev_2.pay, dev_2.unit)
print()

#For Developers
dev_1 = Developer('Innocent', 'Charles', 50000, 'Python')
dev_2 = Developer('Benjamin', 'Ben', 20000, 'Java')

# print(help(Developer))
print(dev_1.first, dev_1.last, dev_1.pay, dev_1.prog_lang)
print(dev_2.email)

print(dev_1.pay)
dev_1.apply_increase_amount()
print(dev_1.pay)


# Lesson 1
class Employee:
  increase_amount = 1.5

  def __init__(self, first, last, pay):
    self.first = first
    self.last = last
    self.pay = pay
    self.email = first + '.' + last + '@email.com'

  def fullname(self):
    return '{} {}'.format(self.first, self.last)

  def apply_increase_amount(self):
     self.pay = int(self.pay * self.increase_amount)

class Developer(Employee):
  increase_amount = 5

dev_1 = Developer('Innocent', 'Charles', 50000)
dev_2 = Developer('Benjamin', 'Ben', 20000)

# print(help(Developer))
# print(dev_1.first)
# print(dev_2.email)

print(dev_1.pay)
dev_1.apply_increase_amount()
print(dev_1.pay)
