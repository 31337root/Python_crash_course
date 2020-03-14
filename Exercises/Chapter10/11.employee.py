import unittest

class Employee():
    """Name and salary"""

    def __init__(self, f_name, l_name, salary):
        """Initialize the class."""
        self.f_name = f_name
        self.l_name = l_name
        self.salary = salary

    def give_raise(self, amount=5000):
        self.salary += amount

class EmployeeTest(unittest.TestCase):
    """Unit testing for Employee class"""

    def setUp(self):
        """Create a employee"""

        self.employee = Employee("Lola", "Moreno", 3000000)

    def test_give_default_raise(self):
        self.employee.give_raise()
        self.assertEqual(self.employee.salary, 3005000)

    def test_give_custom_raise(self):
        self.employee.give_raise(1000000)
        self.assertEqual(self.employee.salary, 4000000)

unittest.main()
