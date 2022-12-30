import re
import numpy as np
from src.chromosome.chromosome import Chromosome
from itertools import permutations


class Population:
    def __init__(self, config: dict, population_size: int, fitness_equation: str = "", generation_limit: int = 5):
        '''

        Args:
            config: chromosome configuration
            population_size: -
            fitness_equation: equation imported from fitness_function.py files
            generation_limit: number of generations (finish condition)
        '''
        self.population_size = population_size
        self.generation_limit = generation_limit

        self.fitness_avg_std = 0  # finish condition
        self.fitness_avg = []  # list of population average fitness in each generation

        # Initialization of population
        self.population = [Chromosome(conf=config) for _ in range(self.population_size)]
        # Setting fitness initialization population
        for chromosome in self.population:
            fitness_val = self._fitness(fitness_equation, chromosome.get_phenotype())
            chromosome.set_fitness(fitness_val)
        self.set_fitness_avg()

    @staticmethod
    def _fitness(equation, phenotype):
        parameters = re.search(r"\(\s*([^)]+?)\s*\)", equation).group(1).replace(" ", "").split(',')
        equ = re.findall(r"=\s*(.+)", equation)[0]

        for param, var in zip(parameters, phenotype):
            exec(f'{param} = {var}')
        result = eval(equ)
        return result

    def get_fitness_sum(self):
        return sum(map(lambda x: float(x.get_fitness()), self.population))

    def set_fitness_avg(self):
        self.fitness_avg.append(self.get_fitness_sum() / self.population_size)

    def set_fitness_std(self):
        if len(self.fitness_avg) > 5:
            self.fitness_avg_std = np.std(self.fitness_avg[-3:])

    def selection_roulette_wheel_method(self):
        probabilities = []

        for chromosome in self.population:
            probabilities.append(
                chromosome.get_fitness() / self.get_fitness_sum())  # list of chromosomes probabilities
        selected_population = np.random.choice(self.population, size=self.population_size,
                                               p=probabilities)
        self.population = selected_population

    def crossover(self, cross_probability: float = 0.7, cross_points_num: int = 1):
        possible_permutations = permutations(range(self.population_size), 2)
        possible_permutations = list(set([tuple(sorted(x)) for x in list(possible_permutations)]))
        rng = np.random.default_rng()
        # cross_chromosomes - lista tupli z chromosomami, ktore sa krzyzowane [(1,4), (1,7), (2,3)] moga sie powtarzac chromosomy
        cross_chromosomes = rng.choice(possible_permutations, int(cross_probability * self.population_size),
                                       replace=False)
        for chrom_a, chrom_b in cross_chromosomes:
            a = self.population[chrom_a].get_genome()
            b = self.population[chrom_b].get_genome()
            cross_points = np.random.randint(len(a), size=cross_points_num)

            for i in cross_points:
                a_new = np.concatenate([a[:i], b[i:]])
                b_new = np.concatenate([b[:i], a[i:]])
                a = a_new
                b = b_new

            self.population[chrom_a].set_genome(a)
            self.population[chrom_b].set_genome(b)

    def mutate(self, mutation_probability: float = 0.1, mutation_type: str = "binary"):
        selected_chromosomes = np.random.choice(self.population, size=int(mutation_probability * self.population_size))
        for chromosome in selected_chromosomes:
            if mutation_type == "binary":
                chromosome.binary_mutate()
            elif mutation_type == "inversion":
                chromosome.inversion_mutate()
            elif mutation_type == "swap":
                chromosome.swap_mutate()
            elif mutation_type == "insert":
                chromosome.insert_mutate()
            elif mutation_type == "relocate":
                chromosome.relocate_mutate()
            else:
                pass
