from turtle import *

shape("turtle")


def draw(width, shapes):
    for a in range(shapes):
        forward(width)
        left(360.0 / shapes)


draw(100, 8)
draw(100, 4)
draw(100, 3)
