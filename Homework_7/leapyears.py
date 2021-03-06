#   Author: Duy Pham
#   Date: 3/7/2021
#   Program:leapyears.py
#   Description: Homework 7
import unittest
import leapyearsTDD
class mod4(unittest.TestCase):
    def test1(self):
        self.assertEqual(leapyearsTDD.leapyear(4),"leap year")

    def test2(self):
        self.assertEqual(leapyearsTDD.leapyear(400),"leap year")

    def test3(self):
        self.assertEqual(leapyearsTDD.leapyear(13),"not leap year")

    def test4(self):
        self.assertEqual(leapyearsTDD.leapyear(2012),"leap year")

    def test5(self):
        self.assertEqual(leapyearsTDD.leapyear(1900),"not leap year")


if __name__ == "__main__":
    unittest.main()
