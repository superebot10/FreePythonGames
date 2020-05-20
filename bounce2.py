"""Bounce, a simple animation demo.

Exercises

1. Change color of ball when it hits a wall
2. Change the curvature of the ball when it hits a wall between -5 and 5
3. Change the speed when ball hits wall

"""
#from turtle import *
import turtle
from base import vector
import random

def value():
    "Randomly generate value between (-5, -3) or (3, 5)."
    return (3 + random.random() * 2) * random.choice([1, -1])

ball = vector(0, 0)
aim = vector(value(), value())
colors = ["red", "green", "blue", "yellow", "purple"]
ballcolor = colors[random.randint(0, 4)]

def draw():
    "Move ball and draw game."
    ball.move(aim * 3)  #speed
    aim.rotate(random.random() * -5) #curvature

    x = ball.x
    y = ball.y

    global ballcolor

    if x < -200 or x > 200:
        aim.x = -aim.x
        ballcolor = colors[random.randint(0, 4)]

    if y < -200 or y > 200:
        aim.y = -aim.y
        ballcolor = colors[random.randint(0, 4)]
    #clear()
    turtle.goto(x, y)
    turtle.dot(10, ballcolor)

    turtle.ontimer(draw, 50)

turtle.setup(420, 420, 370, 0)
turtle.hideturtle()
turtle.tracer(False)
turtle.up()
draw()
turtle.done()
