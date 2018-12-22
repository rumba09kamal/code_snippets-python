import unittest
from unittest.mock import patch
from employee import Employee


class EmployeeTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """ runs once before test starts  """
        print('setUpClass\n')
        pass

    @classmethod
    def tearDownClass(cls):
        """ runs once after test ends """
        print('tearDownClass')
        pass

    def setUp(self):
        """ runs before each test """
        print('setUp')
        self.emp_1 = Employee('Kamal', 'Lama', 100)
        self.emp_2 = Employee('Ram', 'Lama', 1000)

    def tearDown(self):
        """ runs after each test """
        print('tearDown\n')
        pass

    def test_email(self):
        print('test_email')
        self.assertEqual(self.emp_1.email, 'Kamal.Lama@email.com')
        self.assertEqual(self.emp_2.email, 'Ram.Lama@email.com')

        self.emp_1.fname = 'Jhon'
        self.emp_2.fname = 'Jane'

        self.assertEqual(self.emp_1.email, 'Jhon.Lama@email.com')
        self.assertEqual(self.emp_2.email, 'Jane.Lama@email.com')

    def test_fullname(self):
        print('test fullname')
        self.assertEqual(self.emp_1.fullname, 'Kamal Lama')
        self.assertEqual(self.emp_2.fullname, 'Ram Lama')

        self.emp_1.fname = 'Jhon'
        self.emp_2.fname = 'Jane'

        self.assertEqual(self.emp_1.fullname, 'Jhon Lama')
        self.assertEqual(self.emp_2.fullname, 'Jane Lama')

    def test_applyraise(self):
        print('test_apply_raise')
        self.emp_1.apply_raise()
        self.emp_2.apply_raise()
        self.assertEqual(self.emp_1.pay, 105)
        self.assertEqual(self.emp_2.pay, 1050)

        self.emp_1.pay = 50000
        self.emp_2.pay = 60000

        self.emp_1.apply_raise()
        self.emp_2.apply_raise()

        self.assertEqual(self.emp_1.pay, 52500)
        self.assertEqual(self.emp_2.pay, 63000)

    def test_monthly_schedule(self):
        """ patch can be used as function decorator"""
        """ using patch as a context manager """
        with patch('employee.requests.get') as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = 'Success'

            schedule = self.emp_1.monthly_schedule('May')
            mocked_get.assert_called_with('http://company.com/Lama/May')
            self.assertEqual(schedule, 'Success')

            mocked_get.return_value.ok = False

            schedule = self.emp_2.monthly_schedule('April')
            mocked_get.assert_called_with('http://company.com/Lama/April')
            self.assertEqual(schedule, 'Bad Response!')


if __name__ == '__main__':
    unittest.main()
