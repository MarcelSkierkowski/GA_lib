from src.chromosome.chromosome import Chromosome

config = {
    "genes_size": [3, 3, 4],
    "genes_range": [(-2, 5), (0, 7), (-3, 12)],
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

