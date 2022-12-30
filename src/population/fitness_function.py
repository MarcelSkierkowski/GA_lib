import numpy as np


def f_equ(x, y):
    return (x + 0.5) ** 2 + (y + 0.5) ** 2


def f_shaffer(x, y):
    return (x ** 2 + y ** 2) ** 0.25 * (np.sin(50 * (x ** 2 + y ** 2) ** 0.1) + 1)
