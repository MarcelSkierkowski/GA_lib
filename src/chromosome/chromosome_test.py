from chromosome import BinChromosome, TriaChromosome
from mutatoin_functions import bin_mutate, tri_mutate


def mutation_bin():
    gen = BinChromosome(2, 10, bin_mutate)
    gen.generate()
    print(gen)
    gen.mutation()
    print(gen)


def mutation_tri():
    gen = TriaChromosome(2, 10, tri_mutate)
    gen.generate()
    print(gen)
    gen.mutation()
    print(gen)


mutation_tri()
