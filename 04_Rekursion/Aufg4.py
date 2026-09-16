from turtle import *


def koch_curve(steps: int, dist: float):
    if steps <= 1:
        forward(dist)
    else:
        dist /= 3.0
        koch_curve(steps - 1, dist)
        left(60)
        koch_curve(steps - 1, dist)
        right(120)
        koch_curve(steps - 1, dist)
        left(60)
        koch_curve(steps - 1, dist)
        speed(0)

speed(0)
koch_curve(5,300)
mainloop()