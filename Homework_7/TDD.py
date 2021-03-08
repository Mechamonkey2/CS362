
#   Author: Duy Pham
#   Date: 3/7/2021
#   Program:TDD.py
#   Description: Homework 7

import unittest
import TDD_tests

class TestCase(unittest.TestCase):
    def test1(self):
        self.assertEqual(TDD_tests.hello_world(),'Hello World!')

class return_number(unittest.TestCase):
    TDD_tests.print100()
    def test1(self):
        self.assertEqual(TDD_tests.FizzBuzz(3),"fizz")
        self.assertEqual(TDD_tests.FizzBuzz(4),4)

    #def test2(self):
    #    self.assertEqual(TDD_tests.FizzBuzz(i),3)

if __name__ == '__main__':
    unittest.main()
