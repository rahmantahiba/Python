#Cloning the turtle

import turtle 

t = turtle.Turtle()
c = t.clone()
t.color("Red")
c.color("Magenta")
t.circle(100)
c.circle(90)