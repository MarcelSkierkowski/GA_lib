import re
import numpy as np
from src.chromosome.chromosome import Chromosome


class Population:
    def __init__(self, config: dict, population_size: int, fitness_equation: str = "", generation_limit: int = 5):
        self.population_size = population_size
        self.generation_limit = generation_limit

        self.fitness_avg_std = 0  # finish condition
        self.fitness_avg = []  # list of population average fitness in each generation

        self.population = [Chromosome(conf=config) for _ in range(self.population_size)]
        # Setting fitness initialization population
        fitness_sum = 0
        for chromosome in self.population:
            fitness_val = self._fitness(fitness_equation, chromosome.get_phenotype())
            fitness_sum += fitness_val
            chromosome.set_fitness(fitness_val)
        self.fitness_avg.append(fitness_sum / population_size)

    def set_fitness_std(self):
        if len(self.fitness_avg) > 5:
            self.fitness_avg_std = np.std(self.fitness_avg[-3:])

    @staticmethod
    def _fitness(equation, phenotype):
        parameters = re.search(r"\(\s*([^)]+?)\s*\)", equation).group(1).replace(" ", "").split(',')
        equ = re.findall(r"=\s*(.+)", equation)[0]

        for param, var in zip(parameters, phenotype):
            exec(f'{param} = {var}')
        result = eval(equ)
        return result

    def selection_roulette_wheel_method(self):
        probabilities = []

        fitness_sum = sum(map(lambda x: float(x.get_fitness()), self.population))
        for chromosome in self.population:
            probabilities.append(
                chromosome.get_fitness() / fitness_sum)  # list of list with chromosome index and its probability
        selected_population = np.random.choice(self.population, size=self.population_size,
                                               p=probabilities)
        self.population = selected_population

    def crossover_one_point(self):
        pass

    def crossover_multiple_points(self):
        pass
