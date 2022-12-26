import re
import math
from src.chromosome.chromosome import Chromosome


class Population:
    def __init__(self, config: dict, population_size: int, fitness_equation: str = "", generation_limit: int = 5):
        self.population_size = population_size
        self.fitness_avg = []
        self.generation_limit = generation_limit

        self.population = [Chromosome(conf=config) for _ in range(self.population_size)]
        # Setting fitness initialization population
        fitness_sum = 0
        for chromosome in self.population:
            fitness_val = self.fitness(fitness_equation, chromosome.get_phenotype())
            fitness_sum += fitness_val
            chromosome.set_fitness(fitness_val)
        self.fitness_avg.append(fitness_sum / population_size)

    @staticmethod
    def fitness(equation, phenotype):
        parameters = re.search(r"\(\s*([^)]+?)\s*\)", equation).group(1).replace(" ", "").split(',')
        equ = re.findall(r"=\s*(.+)", equation)[0]

        for param, var in zip(parameters, phenotype):
            exec(f'{param} = {var}')
        result = eval(equ)
        return result
