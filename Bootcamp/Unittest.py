import unittest
from unittest.mock import patch
from unitT import Employee

class TestEmployee(unittest.TestCase):

  @classmethod
  def setUpClass(cls):
    print('setupClass')

  @classmethod
  def tearDownClass(cls):
    print('teardownClass')
    
  def setUp(self):
    print('setUp')
    self.emp1 = Employee('Okon', 'Samuel', 50000)
    self.emp2 = Employee('Innocent', 'Charles', 6000)

  def tearDown(self):
    print('tearDown\n')
    
  def test_email(self):
    print('test_email')
    self.assertEqual(self.emp1.email, 'Okon.Samuel@email.com')
    self.assertEqual(self.emp2.email, 'Innocent.Charles@email.com')

    self.emp1.first = 'Mercy'
    self.emp2.first = 'Johnson'

    self.assertEqual(self.emp1.email, 'Mercy.Samuel@email.com')
    self.assertEqual(self.emp2.email, 'Johnson.Charles@email.com')


  def test_fullname(self):
    print('test_fullname')
    self.assertEqual(self.emp1.fullname, 'Okon Samuel')
    self.assertEqual(self.emp2.fullname, 'Innocent Charles')

    self.emp1.first = 'Mercy'
    self.emp2.first = 'Johnson'

    self.assertEqual(self.emp1.fullname, 'Mercy Samuel')
    self.assertEqual(self.emp2.fullname, 'Johnson Charles')

  def test_apply_raise(self):
    print('test_apply_raise')
    self.emp1.apply_raise()
    self.emp2.apply_raise()

    self.assertEqual(self.emp1.pay, 50000)
    self.assertEqual(self.emp2.pay, 6000)

  def test_monthly_schedule(self):
    with patch('employee.requests.get') as mocked_get:
      mocked_get.return_value.ok = True
      mocked_get.return_value.text = 'Success'

      schedule = self.emp1.monthly_schedule('May')
      mocked_get.assert_called_with('http://company.com/Samuel/June')
      self.assertEqual(schedule, 'Success')

      mocked_get.return_value.ok = False
     
      schedule = self.emp1.monthly_schedule('June')
      mocked_get.assert_called_with('http://company.com/Charles/June')
      self.assertEqual(schedule, 'Bad Response!')

if __name__ == '__main__':
  unittest.main()
  
#Lesson 3
import unittest
from unitT import Employee

class TestEmployee(unittest.TestCase):

  def setUp(self):
    print('setUp')
    self.emp1 = Employee('Okon', 'Samuel', 50000)
    self.emp2 = Employee('Innocent', 'Charles', 6000)

  def tearDown(self):
    print('tearDown\n')
    
  def test_email(self):
    print('test_email')
    self.assertEqual(self.emp1.email, 'Okon.Samuel@email.com')
    self.assertEqual(self.emp2.email, 'Innocent.Charles@email.com')

    self.emp1.first = 'Mercy'
    self.emp2.first = 'Johnson'

    self.assertEqual(self.emp1.email, 'Mercy.Samuel@email.com')
    self.assertEqual(self.emp2.email, 'Johnson.Charles@email.com')


  def test_fullname(self):
    print('test_fullname')
    self.assertEqual(self.emp1.fullname, 'Okon Samuel')
    self.assertEqual(self.emp2.fullname, 'Innocent Charles')

    self.emp1.first = 'Mercy'
    self.emp2.first = 'Johnson'

    self.assertEqual(self.emp1.fullname, 'Mercy Samuel')
    self.assertEqual(self.emp2.fullname, 'Johnson Charles')

  def test_apply_raise(self):
    print('test_apply_raise')
    self.emp1.apply_raise()
    self.emp2.apply_raise()

    self.assertEqual(self.emp1.pay, 50000)
    self.assertEqual(self.emp2.pay, 6000)

if __name__ == '__main__':
  unittest.main()


#Lesson 2
import unittest
from unitT import Employee

class TestEmployee(unittest.TestCase):

  def setUp(self):
    self.emp1 = Employee('Okon', 'Samuel', 50000)
    self.emp2 = Employee('Innocent', 'Charles', 6000)

    
  def test_email(self):
    self.assertEqual(self.emp1.email, 'Okon.Samuel@email.com')
    self.assertEqual(self.emp2.email, 'Innocent.Charles@email.com')

    self.emp1.first = 'Mercy'
    self.emp2.first = 'Johnson'

    self.assertEqual(self.emp1.email, 'Mercy.Samuel@email.com')
    self.assertEqual(self.emp2.email, 'Johnson.Charles@email.com')


  def test_fullname(self):
    self.assertEqual(self.emp1.fullname, 'Okon Samuel')
    self.assertEqual(self.emp2.fullname, 'Innocent Charles')

    self.emp1.first = 'Mercy'
    self.emp2.first = 'Johnson'

    self.assertEqual(self.emp1.fullname, 'Mercy Samuel')
    self.assertEqual(self.emp2.fullname, 'Johnson Charles')

  def test_apply_raise(self):
    self.emp1.apply_raise()
    self.emp2.apply_raise()

    self.assertEqual(self.emp1.pay, 50000)
    self.assertEqual(self.emp2.pay, 6000)

if __name__ == '__main__':
  unittest.main()


#Lesson 1
import unittest
from unitT import Employee

class TestEmployee(unittest.TestCase):

  def test_email(self):
    emp1 = Employee('Okon', 'Samuel', 50000)
    emp2 = Employee('Innocent', 'Charles', 6000)

    self.assertEqual(emp1.email, 'Okon.Samuel@email.com')
    self.assertEqual(emp2.email, 'Innocent.Charles@email.com')

    emp1.first = 'Mercy'
    emp2.first = 'Johnson'

    self.assertEqual(emp1.email, 'Mercy.Samuel@email.com')
    self.assertEqual(emp2.email, 'Johnson.Charles@email.com')


  def test_fullname(self):
    emp1 = Employee('Okon', 'Samuel', 50000)
    emp2 = Employee('Innocent', 'Charles', 6000)

    self.assertEqual(emp1.fullname, 'Okon Samuel')
    self.assertEqual(emp2.fullname, 'Innocent Charles')

    emp1.first = 'Mercy'
    emp2.first = 'Johnson'

    self.assertEqual(emp1.fullname, 'Mercy Samuel')
    self.assertEqual(emp2.fullname, 'Johnson Charles')

  def test_apply_raise(self):
    emp1 = Employee('Okon', 'Samuel', 50000)
    emp2 = Employee('Innocent', 'Charles', 6000)

    emp1.apply_raise()
    emp2.apply_raise()

    self.assertEqual(emp1.pay, 50000)
    self.assertEqual(emp2.pay, 6000)

if __name__ == '__main__':
  unittest.main()

# unitT function to be imported by the main function
import requests
class Employee:
  """A simple employee class"""
  raise_amt = 1.05
  def __init__(self, first, last, pay):
    self.first = first
    self.last = last
    self.pay = pay

  @property
  def email(self):
    return '{}.{}@email.com'.format(self.first, self.last)

  @property
  def fullname(self):
    return '{} {}'.format(self.first, self.last)

  def apply_raise(self):
    return int(self.pay * self.raise_amt)

  def monthly_schedule(self, month):
    response = requests.get(f'http://company.com/{self.last}/{month}')
    if response.ok:
      return response.text
    else:
      return 'Bad Response'
  
  
 #Lesson 0 // Call the Calc function
import unittest
import Calc


class TestCalc(unittest.TestCase):

    # def test_add(self):
    #     result = Calc.addition(10, 5)
    #     self.assertEqual(result, 15)

    def test_add(self):
        self.assertEqual(Calc.addition(10, 5), 15)
        self.assertEqual(Calc.addition(-1, 1), 0)
        self.assertEqual(Calc.addition(-1, -1), -2)

    def test_substract(self):
        self.assertEqual(Calc.subtract(10, 5), 5)
        self.assertEqual(Calc.subtract(-1, 1), -2)
        self.assertEqual(Calc.subtract(-1, -1), -0)

    def test_multiply(self):
        self.assertEqual(Calc.multiply(10, 5), 50)
        self.assertEqual(Calc.multiply(-1, 1), -1)
        self.assertEqual(Calc.multiply(-1, -1), 1)

    def test_divide(self):
        self.assertEqual(Calc.divide(10, 5), 2)
        self.assertEqual(Calc.divide(-1, 1), -1)
        self.assertEqual(Calc.divide(-1, -1), 1)

        #self.assertRaises(ValueError, Calc.divide, 10, 0)
        with self.assertRaises(ValueError):
            Calc.divide(10, 0)

if __name__ == '__main__':
    unittest.main()
    
#Calc function to be imported in the main function
 def addition(x, y):
    """Add function"""
    return x + y


def subtract(x, y):
    """Subtract function"""
    return x - y


def multiply(x, y):
    """Multiply function"""
    return x * y

def divide(x, y):
    """Division function"""
    if y == 0:
        raise ValueError('can not divide by 0')
    return x / y
