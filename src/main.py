from numpy.random import rand

from src.chromosome.chromosome import Chromosome
from src.plotter.plotter import plotter_3d, plot_contour, plot_history
from src.population.fitness_function import f_shaffer, f_equ

config = {
    "genes_size": [10, 10],
    "genes_range": [(-5, 5), (-5, 5)],
    "mutation_probability": 0.2
}

population = []

# init population
for _ in range(10):
    chr = Chromosome(conf=config)
    chr.set_fitness(5 * rand())
    population.append(chr)

# get points
x = []
y = []
fitness = []
for chromosome in population:
    x.append(chromosome.get_phenotype()[0])
    y.append(chromosome.get_phenotype()[1])
    fitness.append(chromosome.get_fitness())

# plot
plotter_3d(f_shaffer, (-5, 5, 0.01), (-5, 5, 0.01), (0, 10))
plot_contour(f_shaffer, (-5, 5, 0.01), (-5, 5, 0.01), x, y)

# Tu powinny byc historyczne dane najlepszego chromosomu dla kazdej epoki
plot_history(x, y, fitness)
