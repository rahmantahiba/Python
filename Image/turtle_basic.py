import turtle

#Initializing turtle 

t = turtle.Turtle()

"""

When it's up no lines will be drawn when it moves

When it is down the lines will be drawn when it moves

"""

#Example making a 90 degree angle 

t.right(90)
t.forward(100)
t.left(90)
t.backward(100)

t.goto(100,100)

#Return to home position

t.home()