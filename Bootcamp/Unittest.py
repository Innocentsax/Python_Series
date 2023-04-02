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
