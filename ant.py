"""Ant, simple animation demo.

Exercises

1. Wrap ant around screen boundaries.
2. Make the ant leave a trail.
3. Change the ant color based on position.
   Hint: colormode(255); color(0, 100, 200)

"""

from random import *
from turtle import *
from base import vector

ant = vector(10, 10)
aim = vector(2, 0)

def wrap_x(value):
    if value > 400:
        value = -400
    elif value < -400:
        value = 400
    return value

def wrap_y(value):
    if value > 300:
        value = -300
    elif value < -300:
        value = 300
    return value

def draw():
    "Move ant and draw screen."
    ant.move(aim)
    ant.x = wrap_x(ant.x)
    ant.y = wrap_y(ant.y)
    aim.move(random() - .5)
    aim.rotate(random() * 6)

    #clear()
    goto(ant.x, ant.y)

    if ant.x > 0 and ant.y > 0:
       dot(10, "red")
    elif ant.x < 0 and  ant.y < 0:
       dot(10, "green")
    elif ant.x > 0 and ant.y < 0:
        dot(10, "yellow")
    elif ant.x < 0 and ant.y > 0:
        dot(10, "blue")

    if running:
        ontimer(draw, 100)

setup(800, 600, 100, 0)
hideturtle()
tracer(False)
up()
running = True
draw()
done()
