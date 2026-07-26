import unittest

from employee import Employee

class TestEmployee(unittest.TestCase):
    "Test of the class Employee"

    def setUp(self):
        self.my_employee = Employee("Francisco", "Lopes", 5000)
    
    def test_default_raise(self):
        self.my_employee.give_raise()
        self.assertEqual(self.my_employee.annual_salary, 10000)

    def test_custom_raise(self):
        custom_raise = 1000
        current_salary = self.my_employee.annual_salary
        self.my_employee.give_raise(custom_raise)
        self.assertEqual(self.my_employee.annual_salary, custom_raise + current_salary)

unittest.main()

