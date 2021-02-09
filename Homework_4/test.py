#   Author: Duy Pham
#   Date: 2/8/2021
#   Program:test.py
#   Description: Homework 4-1
import unittest

num_1 = int(input("Enter the first number: "))
num_2 = int(input("Enter the second number: "))
num_3 = int(input("Enter the third number: "))

first_name = input("What is your first name? ")
last_name = input("What is your last name? ")


def cube(a,b,c):
    return a*b*c

class CubeTest(unittest.TestCase):
    def test_1(self):
        a = 1
        b = 1
        c = 1
        self.assertEqual(cube(a,b,c),a*b*c)

    def test_2(self):
        a = -1
        b = 1
        c = 1
        self.assertEqual(cube(a,b,c),-1)

    def test_3(self):
        a = 5.1
        b = -1.9
        c = -3.2
        self.assertEqual(cube(a,b,c),a*b*c)

    def test_4_inputs(self):
        self.assertEqual(cube(num_1,num_2,num_3),num_1*num_2*num_3)

    def test_5_inputs(self):
        self.assertEqual(cube(num_1,num_2,num_3),1313)




###################################################
def average(list):
    sum = 0
    for num in list:
        sum = sum + num
    return  int(sum) / len(list)



class AvgTest(unittest.TestCase):
    def test_1(self):
        list = [1,2,3]
        expected = 2
        self.assertEqual(average(list), expected ,msg='avgList({})'.format(list))

    def test_2(self):
        list = [0,1,2,3]
        expected = 1.5
        self.assertEqual(average(list), expected ,msg='avgList({})'.format(list))

    def test_3(self):
        list = []
        self.assertFalse(list)
        #self.assertRaise(ValueError,average(list))

    def test_4(self):
        list = [0]
        expected = 0
        self.assertEqual(average(list), expected ,msg='avgList({})'.format(list))

    # Test Errors? : To test this works, values 1 2 3 are inputted. Anything else are errors
    def test_5_input(self):
        list = [num_1,num_2,num_3]
        expected = 2
        self.assertEqual(average(list), expected ,msg='avgList({})'.format(list))

##########################################

class People:
    def __init__(self,first,last):
        self.first = first
        self.last = last

    @property
    def fullname(self):
        return '{} {}'.format(self.first,self.last)


class FullName(unittest.TestCase):

    def test_fullname(self):
        Person_1 = People('Duy','Pham')
        self.assertEqual(Person_1.fullname,'Duy Pham')

    def test_fullname(self):
        Person_2 = People('Wolfgang','Puck')
        self.assertEqual(Person_2.fullname,'Wolfgang Puck')

    def test_fullname(self):
        Person_3 = People('Steve','Jobs')
        self.assertEqual(Person_3.fullname,'Steve Jobs')

    ##Test Errors?
    def test_fullname_input(self):
        Person_4 = People(first_name,last_name)
        self.assertEqual(Person_4.fullname,'Gordan Ramsay')
        #You're not Gordan Ramsey !

#Coder Notes: I have no idea what I'm coding. This took a a while. Python is kinda fun, not gonna lie, but I still have no idea what I'm doing.


if __name__ == "__main__":
    unittest.main()
