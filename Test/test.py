"""
Program: test.py
Author:  Luke Xiong
Date: 7/4/2020

This program is a test of the class
.
"""
import unittest
from class_definitions import student


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.student = student.Student('Duck', 'Daisy', 'Science')

    def tearDown(self):
        del self.student
    #test required attributes
    def test_initial_value_required_attributes(self):
        self.assertEqual(self.student.last_name, 'Duck')
        self.assertEqual(self.student.first_name, 'Daisy')
        self.assertEqual(self.student.major, 'Science')

    #test all attributes
    def test_display(self):
        self.assertEqual(str(self.student1), "Duck, Donald has major: Science with gpa: 0.0")

    #Write unit test test_student_str(self)
    def test_student_str(self):
        self.assertEqual(str(self.student), "Duck, Daisy has major: Science with gpa: 0.0")

#Write unit test test_object_not_created_error_last_name(self) that expect exception raised.
    def test_object_not_created_error_last_name(self):
        with self.assertRaises(ValueError):
            p = student.Student(444, 'Daisy')

#Write test_object_not_created_error_first_name(self)
    def test_object_not_created_error_fist_name(self):
        with self.assertRaises(ValueError):
            p = student.Student('Duck', 123)

#Write test_object_not_created_error_major(self)
    def test_object_not_created_error_major(self):
        with self.assertRaises(ValueError):
            p = student.Student('Duck', 'Daisy', 111)

#Write test_object_not_created_error_gpa(self)
    def test_object_not_created_error_major(self):
        with self.assertRaises(ValueError):
            p = student.Student('Duck', 'Daisy', 'Science', 'abc')

if __name__ == '__main__':
    unittest.main()
