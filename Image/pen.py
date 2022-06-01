#Picking the pen up and down in turtle

import turtle

t = turtle.Turtle()

t.speed(2)

t.forward(100)
t.right(90)
t.penup() #Makes sure the object is not drawn repeatedly
t.forward(100)
t.right(90)
t.pendown() #Previous drawing state and draws the picture/shape
t.fd(100)
t.right(90)
t.penup()
t.forward(100)
t.pendown()

#Clearing the screen

t.clear()