#   Author: Duy Pham
#   Date: 3/7/2021
#   Program:leapyears.py
#   Description: Homework 7
import unittest
import leapyearsTDD
class mod4(unittest.TestCase):
    def test1(self):
        self.assertEqual(4,"leap year")

    def test2(self):
        self.assertEqual(100,"leap year")


if __name__ == "__main__":
    unittest.main()
