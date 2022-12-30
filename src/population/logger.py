import math
import re
import numpy as np
from src.chromosome.chromosome import Chromosome
from matplotlib.ticker import LinearLocator
import matplotlib.pyplot as plt
import matplotlib
from matplotlib import cm

matplotlib.use('TkAgg')


class Logger:
    def __init__(self, config: dict, fitness_func, generation_limit: int = 5):
        self.genes_range = config['genes_range']
        self.fitness_func = fitness_func
        self.generation_list = np.arange(generation_limit)
        self.best_chromosome_fitness = []
        self.best_chromosome_phenotype = []

    def save(self, chromosome: Chromosome):
        self.best_chromosome_fitness.append(chromosome.get_fitness())
        self.best_chromosome_phenotype.append(chromosome.get_phenotype())

    def plot(self, num_of_generation):
        x1 = np.arange(*self.genes_range[0])
        x2 = np.arange(*self.genes_range[1])
        x1, x2 = np.meshgrid(x1, x2)
        # y = [self.fitness_func(x1, x2) for x1, x2 in zip(x1, x2)]
        y = self.fitness_func(x1, x2)
        # y = np.sqrt(x1**2 + x2**2)
        fig1, ax1 = plt.subplots(subplot_kw={"projection": "3d"})

        surf = ax1.plot_surface(x1, x2, y, cmap=cm.coolwarm,
                                linewidth=0, antialiased=False)
        ax1.zaxis.set_major_formatter('{x:.02f}')

        fig2 = plt.figure()
        ax2 = plt.axes(projection='3d')
        c1 = np.array(self.best_chromosome_phenotype)[:, 0]
        c2 = np.array(self.best_chromosome_phenotype)[:, 1]
        ax2.plot3D(c1, c2, np.arange(num_of_generation), "red")
        plt.show()
