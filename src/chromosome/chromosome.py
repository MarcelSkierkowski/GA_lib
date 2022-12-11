import numpy as np


class Chromosome:
    def __init__(self, num_alleles, num_genomes, mutate_function):
        self.num_alleles = num_alleles
        self.num_genomes = num_genomes

        self.genome = None
        self.fitness = 0

        self.mutate_function = mutate_function

    def set_fitness(self, fitness):
        self.fitness = fitness

    def set_genome(self, genome):
        if len(genome) != self.num_genomes or len(genome[0]) != self.num_alleles:
            raise Exception(f"Wrong size of genome. Correct is: {self.num_genomes=}, {self.num_alleles}")

        self.genome = genome

    def mutate(self, probability):
        self.mutate_function(self.genome, probability)

    def __str__(self):
        string_allel = '[ '
        for allel in self.genome:
            string_allel = string_allel + str(allel) + ' '
        string_allel = string_allel + ']'
        return string_allel


class BitstringChromosome(Chromosome):
    def __init__(self, num_alleles, num_genomes, mutate_function):
        super().__init__(num_alleles, num_genomes, mutate_function)

        self.randomize()

    def randomize(self):
        self.genome = np.random.randint(low=0, high=2, size=(self.num_genomes, self.num_alleles), dtype=int)


class FloatChromosome(Chromosome):
    def __init__(self, num_alleles, num_genomes, mutate_function, min_value, max_value):
        super().__init__(num_alleles, num_genomes, mutate_function)

        self.min_value = min_value
        self.max_value = max_value

        self.randomize()

    def randomize(self):
        self.genome = np.random.uniform(low=self.min_value, high=self.max_value,
                                        size=(self.num_genomes, self.num_alleles))


class GrayCodeChromosome(Chromosome):
    def __init__(self, num_alleles, num_genomes, mutate_function):
        super().__init__(num_alleles, num_genomes, mutate_function)

        self.randomize()

    def randomize(self):
        # Generate a random binary genome
        binary_genome = np.random.randint(low=0, high=2, size=(self.num_genomes, self.num_alleles), dtype=int)
        self.genome = []
        for genome in binary_genome:
            self.genome.append(self.bin_to_gray(genome))

    @staticmethod
    def bin_to_gray(genome):
        gray_code_genome = [genome[0]]
        for i in range(1, len(genome)):
            gray_code_genome.append(gray_code_genome[i - 1] ^ genome[i])
        return gray_code_genome


# def mutateGray(genome, probability):
#     for i in range(len(genome)):
#         for j in range(len(genome[i])):
#             if np.random.rand() < probability:
#                 genome[i][j] = 1 - genome[i][j]

class TriAlleleChromosome(Chromosome):
    def __init__(self, num_alleles, num_genomes, mutate_function, alleles=None):
        super().__init__(num_alleles, num_genomes, mutate_function)

        if alleles is None:
            alleles = [-1, 0, 1]

        elif len(alleles) != 3:
            raise ValueError("Number of alleles must be 3")

        self.alleles = alleles

        self.randomize()

    def randomize(self):
        self.genome = [np.random.choice(self.alleles, size=self.num_alleles) for _ in range(self.num_genomes)]


class IntegerChromosome(Chromosome):
    def __init__(self, num_alleles, num_genomes, mutate_function, min_value, max_value):
        super().__init__(num_alleles, num_genomes, mutate_function)

        self.min_value = min_value
        self.max_value = max_value

        self.randomize()

    def randomize(self):
        self.genome = np.random.randint(low=self.min_value, high=self.max_value + 1,
                                        size=(self.num_genomes, self.num_alleles))


# def mutateINT(genome, probability):
#     for i in range(len(genome)):
#         for j in range(len(genome[i])):
#             if np.random.rand() < probability:
#                 genome[i][j] += np.random.randint(low=-1, high=2)


class LayeredChromosome(Chromosome):
    def __init__(self, num_layers, num_alleles, num_genomes, mutate_function):
        super().__init__(num_layers * num_alleles, num_genomes, mutate_function)

        self.num_layers = num_layers
        self.num_alleles = num_alleles

        self.randomize()

    def randomize(self):
        self.genome = [[np.random.randint(low=0, high=2, size=self.num_alleles) for _ in range(self.num_layers)] for _
                       in range(self.num_genomes)]


# def mutateLayer(genome, probability):
#     for i in range(len(genome)):
#         for j in range(len(genome[i])):
#             if np.random.rand() < probability:
#                 genome[i][j] = 1 - genome[i][j]


class LogChromosome(BitstringChromosome):
    def __init__(self, num_alleles, num_genomes, mutate_function):
        if num_alleles < 3:
            raise Exception("LogChromosome num_alleles must be 3 or greater")

        super().__init__(num_alleles, num_genomes, mutate_function)

        self.randomize()

    def get_value(self):
        out = []
        for bitstream in self.genome:
            out.append([(-1) ** bitstream[0] * np.exp((-1) ** bitstream[1] * self.bin_to_dec(bitstream[2:]))])
        return out

    @staticmethod
    def bin_to_dec(binary):
        i = 0
        dec = 0
        binary = np.fliplr([binary])

        for bit in binary[0]:
            dec = dec + 2 ** i * bit
            i += 1
        return dec