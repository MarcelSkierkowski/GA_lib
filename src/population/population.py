import numpy as np
from src.chromosome.chromosome import Chromosome
from itertools import permutations, combinations


class Population:
    def __init__(self, config: dict, population_size: int, fitness_func):
        """

        Args:
            config: chromosome configuration
            population_size: -
            fitness_func: function imported from fitness_function.py files
        """
        self.population_size = population_size
        self.fitness_func = fitness_func

        self.fitness_avg_std = -1  # finish condition
        self.fitness_avg = []  # list of population average fitness in each generation

        # Initialization of population
        self.chr_config = config
        self.population = [Chromosome(conf=config) for _ in range(self.population_size)]
        # Setting fitness initialization population
        self.update_fitness()
        self.global_best_chrom = self.get_best_chromosome()

        self.append_fitness_avg()

    def find_best(self):
        candidate = self.get_best_chromosome()
        if candidate.get_fitness() > self.global_best_chrom.get_fitness():
            self.global_best_chrom = candidate

    def update_fitness(self):
        for chromosome in self.population:
            fitness_val = self.fitness_func(*chromosome.get_phenotype())
            chromosome.set_fitness(fitness_val)

    def get_best_chromosome(self):
        index = 0
        for idx, chromosome in enumerate(self.population):
            if chromosome.get_fitness() > self.population[index].get_fitness():
                index = idx
        return self.population[index]

    def get_fitness_sum(self):
        return sum(map(lambda x: float(x.get_fitness()), self.population))

    def append_fitness_avg(self):
        self.fitness_avg.append(self.get_fitness_sum() / self.population_size)

    def set_fitness_std(self):
        if len(self.fitness_avg) > 5:
            self.fitness_avg_std = np.std(self.fitness_avg[-3:])

    def selection_roulette_wheel_method(self):
        probabilities = []
        fitness_sum = self.get_fitness_sum()

        for chromosome in self.population:
            probabilities.append(chromosome.get_fitness() / fitness_sum)

        selected_population = np.random.choice(self.population, size=self.population_size, p=probabilities)

        self.population = selected_population

    def crossover(self, cross_probability: float = 0.7, cross_points_num: int = 1):
        possible_permutations = permutations(range(self.population_size), 2)
        possible_permutations = list(set([tuple(sorted(x)) for x in list(possible_permutations)]))
        rng = np.random.default_rng()
        cross_chromosomes = rng.choice(possible_permutations, self.population_size,
                                       replace=False)

        new_population = []
        for chrom_a, chrom_b in cross_chromosomes:
            a = self.population[chrom_a].get_genome()
            b = self.population[chrom_b].get_genome()
            new_population.append(self._n_points_cross(cross_points_num=cross_points_num, genome_a=a, genome_b=b))

        self.population = new_population

    def _n_points_cross(self, cross_points_num: int, genome_a, genome_b) -> Chromosome:
        if cross_points_num < 1:
            raise Exception("[CROSSOVER]: cross_point_num must be positive integer")

        cross_points = np.random.randint(len(genome_a), size=cross_points_num)

        genome_a_new = []
        for idx in cross_points:
            genome_a_new = np.concatenate([genome_a[:idx], genome_b[idx:]])
            genome_b_new = np.concatenate([genome_b[:idx], genome_a[idx:]])
            genome_a = genome_a_new
            genome_b = genome_b_new

        child = Chromosome(conf=self.chr_config)
        child.set_genome(genome_a_new)

        return child

    def mutate(self, mutation_type: str = "binary"):
        for chromosome in self.population:
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
