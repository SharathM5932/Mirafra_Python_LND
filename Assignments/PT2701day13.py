#  turtle, assert, unit-testing
# use terminal to test
# class Calculator:
#     def add(self,a,b):
#         return a+b
#
# def test_add():
#     calculator=Calculator()
#     a,b=5,3
#     result=calculator.add(a,b)
#     assert result==8,"should be 9" #meaning is test, we can also give message

# import unittest
# def anuroop(lst):
#     return lst[0]+lst[1]+lst[2]
#
# class TestSum(unittest.TestCase):
#        def test_sum(self):
#               self.assertEqual(anuroop([1, 2, 3]), 6, "Should be 6")
#        def test_sum_tuple(self):
#               self.assertEqual(anuroop((2, 2, 2)), 6, "Should be 6")
# if __name__ == '__main__':
#        unittest.main()

# import unittest
#
# class TestStringMethods(unittest.TestCase):
#
#     def test_upper(self):
#         self.assertEqual('dee'.upper(), 'DEE')
#
#     def test_isupper(self):
#         self.assertTrue('DEE'.isupper())
#         self.assertFalse('DEE'.isupper())
#
#     def test_split(self):
#         s = 'hello world'
#         self.assertEqual(s.split(), ['hello', 'world'])
#         # check that s.split fails when the separator is not a string
#         with self.assertRaises(TypeError):
#             s.split(2)
#
# if __name__ == '__main__':
#     unittest.main()












# import turtle
# t=turtle.Pen()
# colors=['red','blue','green']
# for x in range(10):
#     t.color(colors[0])
#     t.forward(100)
#     t.left(90)
# #     t.forward(100)
# #     t.left(90)
# #     t.forward(100)
# #     t.left(90)
# #     t.forward(100)
# #     t.left(90)
# #     t.end_fill()
# #
#
# #Turtle race
# import time
# import turtle
# from turtle import Turtle
# from random import randint
#
# #background
# window=turtle.Screen()
# window.title("Race")
# turtle.bgcolor("palegreen")
# turtle.penup()
# turtle.setpos(-75,300)
# turtle.penup()
# turtle.write("Race", font=("Ariel",30,"bold"))
#
# #finish line
# st=20
# sq=15
# fl=400
# turtle.color("black")
# turtle.shape("square")
# turtle.shapesize(sq/st)
# turtle.penup()
#
# for i in range(10):
#     turtle.setpos(fl,(100-(i*sq*2)))
#     turtle.stamp()
#
# for j in range(10):
#     turtle.setpos(fl+sq,((100-sq)-(j*sq*2)))
#     turtle.stamp()
#
# turtle.hideturtle()
#
# #Turtles
# turtle1=Turtle()
# turtle1.speed(0)
# turtle1.color("black")
# turtle1.shape("turtle")
# turtle1.penup()
# turtle1.goto(-350,60)
# turtle1.pendown()
#
# turtle2=Turtle()
# turtle2.speed(0)
# turtle2.color("yellow")
# turtle2.shape("turtle")
# turtle2.penup()
# turtle2.goto(-350,-10)
# turtle2.pendown()
#
# turtle3=Turtle()
# turtle3.speed(0)
# turtle3.color("black")
# turtle3.shape("turtle")
# turtle3.penup()
# turtle3.goto(-350,-80)
# turtle3.pendown()
#
# time.sleep(1)
#
# #move
# for i in range(245):
#     turtle1.forward(randint(1,15))
#     turtle2.forward(randint(1,5))
#     turtle3.forward(randint(1,5))
#
# turtle.exitonclick()








