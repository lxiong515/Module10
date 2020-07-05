"""
Program: test.py
Author:  Luke Xiong
Date: 7/4/2020

This program is a test of the class
.
"""
import unittest
from class_definitions import person_one as t


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.person_one = t.Person('Duck', 'Daisy')

    def tearDown(self):
        del self.person_one

    def test_initial_value_required_attributes(self):
        self.assertEqual(self.person_one.last_name, 'Duck')
        self.assertEqual(self.person_one.first_name, 'Daisy')

    def test_inital_all_attributes(self):
        person = t.Person('Duck', 'Daisy', '111-11-1111') # this is not self.person from setUp, but local
        assert t.last_name == 'Duck'                 # note no self here on person or assert
        assert t.first_name == 'Daisy'
        assert t.ssn == '111-11-1111'

    def test_object_not_created_error_last_name(self):
        with self.assertRaises(ValueError):
            p = t.Person('123', 'Daisy')

    def test_object_not_created_error_fist_name(self):
        with self.assertRaises(ValueError):
            p = t.Person('Duck', '123')

    def test_object_not_created_error_ssn(self):
        with self.assertRaises(ValueError):
            p = t.Person('Duck', 'Daisy', 'abc')

    def test_person_class_display_name(self):
        self.assertEqual(str(self.person), "Duck, Daisy:")   # Uses person from setUp()

    def test_person_class_display_name_ssn(self):
        p = t.Person('Duck', 'Daisy', '111-11-1111')    # Does not use person from setUp(), has local p
        self.assertEqual(str(p), "Duck, Daisy:111-11-1111")

    def test_person_str(self):
        self.assertEqual(str(self.person), 'Duck, Daisy:')

if __name__ == '__main__':
    unittest.main()
