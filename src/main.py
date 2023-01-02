import matplotlib.pyplot as plt

from src.plotter.plotter import plot_contour, plotter_3d
from src.population.population import Population
from src.population.fitness_function import *

EPOCHS = 200
OPT_FUNCTION = f_multimodal


def main():
    avg = []

    config = {
        "genes_size": [35, 35],
        "genes_range": [(0, 10), (0, 10)],
        "mutation_probability": 0.01
    }

    population = Population(config, population_size=60, fitness_func=OPT_FUNCTION)

    for _ in range(EPOCHS):
        avg.append(population.get_fitness_sum() / population.population_size)

        # Selection
        # population.selection_roulette_wheel_method()
        # population.selection_rank_method()
        # population.selection_tournament_ranking_method()
        population.selection_threshold_method()
        # Crossover
        population.crossover(cross_probability=0.8, cross_points_num=2)
        # Mutation
        population.mutate()

        population.update_fitness()

        population.find_best()

        # Stop condition
        population.append_fitness_avg()
        population.set_fitness_std()
        population.fitness_avg_std = -1  # na razie wylaczylem ten warunek

    plt.plot(avg)
    plt.show()

    x = []
    y = []

    for chrom in population.population:
        x.append(chrom.get_phenotype()[0])
        y.append(chrom.get_phenotype()[1])

    print(population.global_best_chrom.get_phenotype())
    plotter_3d(OPT_FUNCTION, (0, 10, 0.01), (0, 10, 0.01), (0, 15))
    plot_contour(OPT_FUNCTION, config["genes_range"][0], config["genes_range"][1], x, y)


if __name__ == '__main__':
    main()
