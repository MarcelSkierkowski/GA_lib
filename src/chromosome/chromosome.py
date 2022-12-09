import numpy as np


def bin_to_dec(binary: list):
    i = 0
    dec = 0
    binary = np.fliplr([binary])

    for bit in binary[0]:
        dec = dec + 2 ** i * bit
        i += 1
    return dec


class Chromosome:

    def __init__(self, number_of_alles: int, allel_len: int, mutate_fun):
        self.fitness = 0
        self.number_of_allels = number_of_alles
        self.allel_len = allel_len
        self.fenotype = np.array((self.number_of_allels, self.allel_len))
        self.allowed_allels = (0, 0)
        self.mutate_fun = mutate_fun

    def generate(self):
        self.fenotype = np.random.randint(low=self.allowed_allels[0], high=self.allowed_allels[-1] + 1,
                                          size=(self.number_of_allels, self.allel_len), dtype=int)

    def mutation(self):

        if self.fenotype is None:
            raise Exception("Fenotype is Nonne")

        self.fenotype = self.mutate_fun(chromosome=self.fenotype, r_mut=0.1)

    def __str__(self):
        string_allel = '[ '
        for allel in self.fenotype:
            string_allel = string_allel + str(allel) + ' '
        string_allel = string_allel + ']'
        return string_allel


class BinChromosome(Chromosome):

    def __init__(self, number_of_alles, allel_len, mutate_fun):
        super().__init__(number_of_alles, allel_len, mutate_fun)

        self.allowed_allels = (0, 1)


class GrayChromosome(BinChromosome):
    def __init__(self, number_of_alles, allel_len, mutate_fun):
        super().__init__(number_of_alles, allel_len, mutate_fun)

    def generate(self):
        pass


class LogChromosome(BinChromosome):

    def __init__(self, number_of_alles, allel_len, mutate_fun):
        if allel_len < 3:
            raise Exception("Log Chromosome size must be 3 or greater")

        super().__init__(number_of_alles, allel_len, mutate_fun)

    def get_value(self):
        out = []
        for bitstream in self.fenotype:
            out.append([(-1) ** bitstream[0] * np.exp((-1) ** bitstream[1] * bin_to_dec(bitstream[2:]))])
        return out


class TriaChromosome(Chromosome):

    def __init__(self, number_of_alles, allel_len, mutate_fun):
        super().__init__(number_of_alles, allel_len, mutate_fun)

        self.allowed_allels = (-1, 0, 1)


class IntChromosome(Chromosome):
    pass


class LayerChromosome(Chromosome):
    pass
