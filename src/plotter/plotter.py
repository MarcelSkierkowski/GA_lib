import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm


def plotter_3d(function_3d, x_range, y_range, z_range):
    fig, ax = plt.subplots(subplot_kw={"projection": "3d"})

    x = np.arange(*x_range)
    y = np.arange(*y_range)
    X, Y = np.meshgrid(x, y)

    Z = function_3d(X, Y)

    surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm, linewidth=0, antialiased=False)

    ax.set_zlim(*z_range)
    fig.colorbar(surf, shrink=0.5, aspect=5)

    plt.show()


def plot_contour(function_3d, x_range, y_range, points_x, points_y):
    plt.figure()

    x = np.arange(*x_range)
    y = np.arange(*y_range)
    X, Y = np.meshgrid(x, y)

    Z = function_3d(X, Y)

    plt.contour(X, Y, Z)
    plt.plot(points_x, points_y, 'ro')
    plt.show()


def plot_history(x, y, z):
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    ax.scatter(x, y, z, marker='o', c='red')
    ax.plot3D(x,y,z)

    plt.show()

