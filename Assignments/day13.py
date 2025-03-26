import turtle
star = turtle.Turtle()
for i in range(50):
   star.forward(50)
   star.left(144)
turtle.done()
from turtle import *
color('red', 'yellow')
begin_fill()
while True:
   forward(200)
   left(170)
   if abs(pos()) < 1:
      break
end_fill()
done()
class Calculator():
    def add(self,a,b):
        return a+b
def test_add():
    # Arrange
    calculator = Calculator()
    a,b = 5,5
    # Act
    result = calculator.add(a, b)
    # Assert
    assert result == 10
test_add()
import unittest
class TestSum(unittest.TestCase):
       def test_sum(self):
              self.assertEqual(sum([1, 2, 3]), 6, "Should be 6")
       def test_sum_tuple(self):
              self.assertEqual(sum((1, 2, 2)), 5, "Should be 6")
if __name__ == '__main__':
       unittest.main()
import unittest
class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('dee'.upper(), 'DEE')

    def test_isupper(self):
        self.assertTrue('DEE'.isupper())
        self.assertFalse('DEE'.islower())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()
