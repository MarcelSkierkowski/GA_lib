import math


def f_equ(x, y, z):
    return (x + 0.5) ** 2 + (y + 0.5) ** 2 + z


def f_shaffer(x, y):
    return (x ** 2 + y ** 2) ** 0.25 * (math.sin(50 * (x ** 2 + y ** 2) ** 0.1) + 1)
