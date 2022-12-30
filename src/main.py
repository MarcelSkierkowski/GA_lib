from src.chromosome.chromosome import Chromosome
from src.population.population import Population
from src.population.logger import Logger
from src.population.fitness_function import *

config = {
    "genes_size": [24, 24],
    "genes_range": [(-100, 100), (-100, 100)],
    "mutation_probability": 0.2
}


# chromosome = Chromosome(conf=config)
# print("\n\nChromosome jest lista bitow ale w reprezentacji dorysowuje nawiasy w celu latwego zobrazowania "
#       "poszczegolnych genow\n")
# print(f"Chromosome: {chromosome}")
# chromosome.binary_mutate()
# print(f"Chromosome after mutation {chromosome}")
# print("\nWartosci po przeskalowaniu")
# print(chromosome.get_phenotype())
#
# chromosome.set_fitness(0.5)
# print(f"\nFitness: {chromosome.get_fitness()}")

def main():
    population_one = Population(config, population_size=60, fitness_func=f_equ, generation_limit=50)
    logs = Logger(config, fitness_func=f_equ)
    i = 0
    while not (i > population_one.generation_limit or -1 < population_one.fitness_avg_std < 0.0001):
        # Selection
        population_one.selection_roulette_wheel_method()
        # Crossover
        population_one.crossover(cross_probability=0.8, cross_points_num=2)
        # Mutation
        population_one.mutate(mutation_probability=0.01)
        # Stop condition
        population_one.append_fitness_avg()
        population_one.set_fitness_std()

        print(f"Generation {i}: population fitness average standard deviation {population_one.fitness_avg_std:.3f}")
        logs.save(population_one.get_best_chromosome())

        population_one.fitness_avg_std = -1 # na razie wylaczylem ten warunek
        i += 1

    logs.plot(num_of_generation=i)


if __name__ == '__main__':
    main()
