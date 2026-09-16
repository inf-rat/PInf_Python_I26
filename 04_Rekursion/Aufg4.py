import turtle
from tkinter import mainloop


def koch_curve(steps: int, dist: float):
    if steps <= 1:
        turtle.forward(dist)
    else:
        dist /= 3.0
        koch_curve(steps - 1, dist)
        turtle.left(60)
        koch_curve(steps - 1, dist)
        turtle.right(120)
        koch_curve(steps - 1, dist)
        turtle.left(60)
        koch_curve(steps - 1, dist)
        turtle.speed(0)

turtle.speed(0)
koch_curve(5,300)
mainloop()