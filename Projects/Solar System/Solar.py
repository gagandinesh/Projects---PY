# pip install pythonTurtle

# pip install python-math

import turtle
import math
from math import *

# Create screen
screen = turtle.Screen()
screen.tracer(50)

# create SUN

sun = turtle.Turtle()
sun.shape("circle")
sun.color("Orange")


# create  planet
class planet(turtle.Turtle):
    def __init__(self, name, radius, color):
        super().__init__(shape="circle")
        self.name = name
        self.radius = radius
        self.c = color
        self.color(self.c)
        self.up()
        self.pd()
        self.angle = 0

    def move(self):
        x = self.radius * cos(self.angle)
        y = self.radius * sin(self.angle)
        self.goto(sun.xcor() + x, sun.ycor() + y)  # x and y are coridinates

        # making Planets


Mercury = planet("Mercury", 40, "Grey")
Venus = planet("Venus", 80, "Yellow")
Earth = planet("Earth", 100, "Blue")
Mars = planet("Mars", 150, "Red")
Jupiter = planet("jupter", 180, "Brown")
Saturn = planet("Saturn", 230, "pink")
Uranus = planet("Uranus", 250, "purple")
Neptune = planet("Neptune", 280, "Black")

# Add the Planet to List created

myList = [Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, Neptune]

while True:
    screen.update()
    for i in myList:
        i.move()

        # increse the lengtht angle by 0.0x radian
    Mercury.angle += 0.05
    Venus.angle += 0.03
    Earth.angle += 0.01
    Mars.angle += 0.007
    Jupiter.angle += 0.02
    Saturn.angle += 0.018
    Uranus.angle += 0.016
    Neptune.angle += 0.005
