from numpy.random import rand, choice
import numpy as np
import random


def bin_mutate(chromosome=None, r_mut=0.01):
    chromosome_out = chromosome.copy()

    for bitstream in chromosome_out:
        for i in range(len(bitstream)):
            if rand() < r_mut:
                bitstream[i] = 1 - bitstream[i]
    return chromosome_out


def tri_mutate(chromosome=None, r_mut=0.01):
    chromosome_out = chromosome.copy()

    for bitstream in chromosome_out:
        for i in range(len(bitstream)):
            if rand() < r_mut:
                possible_values = [-1, 0, 1]
                possible_values.remove(bitstream[i])
                bitstream[i] = choice(possible_values)
    return chromosome_out


def inversion(chromosome=None, r_mut=0.01):
    chromosome_out = chromosome.copy()

    if rand() < r_mut:
        number_of_genes = len(chromosome_out)

        start = random.randint(0, (number_of_genes - 2))
        stop = random.randint(start, (number_of_genes - 1))

        inverse = np.flipud(chromosome_out[start:stop + 1])
        chromosome_out[start:stop + 1] = inverse

    return chromosome_out


def exchange(chromosome=None, r_mut=0.01, k=1):
    chromosome_out = chromosome.copy()

    if rand() < r_mut:
        number_of_genes = len(chromosome_out)
        for _ in range(k):
            first = random.randint(0, (number_of_genes - 1))
            second = random.randint(0, (number_of_genes - 1))

            chromosome_out[[first, second]] = chromosome_out[[second, first]]
    return chromosome_out


def replace(chromosome=None, r_mut=0.01):
    chromosome_out = chromosome.copy()

    if rand() < r_mut:
        number_of_genes = len(chromosome_out)
        start = random.randint(0, (number_of_genes - 2))
        stop = random.randint(start, (number_of_genes - 1))
        print(start, stop)
        chromosome_out = np.vstack((chromosome_out[0:start], chromosome_out[start + 1:stop + 1], chromosome_out[start],
                                    chromosome_out[stop + 1:]))
    return chromosome_out
