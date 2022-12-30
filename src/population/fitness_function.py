import math


def f_equ(x, y):
    return (x + 0.5) ** 2 + (y + 0.5) ** 2


def f_shaffer(x, y):
    return (x ** 2 + y ** 2) ** 0.25 * (math.sin(50 * (x ** 2 + y ** 2) ** 0.1) + 1)


EQUATION = "f(x, y) = (math.floor(x + 0.5))**2 + (math.floor(y + 0.5))**2"
SHAFFER_EQUATION = "f(x, y) = (x**2 + y**2)**(0.25) * (math.sin(50*(x**2 + y**2)**(0.1)) + 1)"
