
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
    def test1(self):
        self.assertEqual(TDD_tests.FizzBuzz(1),1)

    for i in range(1,11):
        while(i<=100):
            print(i," ", end ="")
            i+=10
        print()

if __name__ == '__main__':
    unittest.main()
