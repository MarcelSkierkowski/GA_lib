from numpy.random import rand, choice


def bin_mutate(chromosome=None, r_mut=0.01):
    if type(chromosome) is None:
        raise Exception("[bin_mutation]: Chromosome can't be a NoneType")

    chromosome_out = chromosome.copy()

    for bitstream in chromosome_out:
        for i in range(len(bitstream)):
            if rand() < r_mut:
                bitstream[i] = 1 - bitstream[i]
    return chromosome_out


def tri_mutate(chromosome=None, r_mut=0.01):
    if type(chromosome) is None:
        raise Exception("[bin_mutation]: Chromosome can't be a NoneType")

    chromosome_out = chromosome.copy()

    for bitstream in chromosome_out:
        for i in range(len(bitstream)):
            if rand() < r_mut:
                possible_values = [-1, 0, 1]
                possible_values.remove(bitstream[i])
                bitstream[i] = choice(possible_values)
    return chromosome_out
