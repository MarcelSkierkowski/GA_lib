from src.chromosome.chromosome import Chromosome
from src.population.population import Population
from src.population.fitness_function import *

config = {
    "genes_size": [3, 3, 4],
    "genes_range": [(-5, 5), (-5, 7), (0, 12)],
    "mutation_probability": 0.2
}

chromosome = Chromosome(conf=config)
print("\n\nChromosome jest lista bitow ale w reprezentacji dorysowuje nawiasy w celu latwego zobrazowania "
      "poszczegolnych genow\n")
print(f"Chromosome: {chromosome}")
chromosome.binary_mutate()
print(f"Chromosome after mutation {chromosome}")
print("\nWartosci po przeskalowaniu")
print(chromosome.get_phenotype())

chromosome.set_fitness(0.5)
print(f"\nFitness: {chromosome.get_fitness()}")

population_one = Population(config, population_size=10, fitness_equation=EQUATION, generation_limit=10)
i = 0
while i < population_one.generation_limit or 0 < population_one.fitness_avg_std < 0.5:
    # Selection
    population_one.selection_roulette_wheel_method()

    i += 1
