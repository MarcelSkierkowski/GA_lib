import numpy as np


def f_equ(x, y):
    return (x + 0.5) ** 2 + (y + 0.5) ** 2


def f_shaffer(x, y):
    return (x ** 2 + y ** 2) ** 0.25 * (np.sin(50 * (x ** 2 + y ** 2) ** 0.1) + 1)


def f_easom(x, y):
    return np.cos(x) * np.cos(y) * np.exp(-(x - np.pi) ** 2 - (y - np.pi) ** 2) + 0.1


def f_multimodal(x, y):
    a1 = [4, 1, 8, 6, 7]
    a2 = [4, 1, 8, 6, 3]
    c1 = [0.1, 0.2, 0.2, 0.4, 0.6]

    val = 0
    for a, b, c in zip(a1, a2, c1):
        val += ((x - a) ** 2 + (y - b) ** 2 + c) ** -1

    return val


def ones(x, y):
    return x + y
