from numpy.random import rand, randint
from cerberus import Validator

from src.chromosome.configuration_schema import schema


class Chromosome:
    def __init__(self, conf: dict):
        is_ok, err = self._validate_config(conf)
        if not is_ok:
            raise Exception(err)

        self._genome = []
        self._fitness = 0

        self._genes_size = conf["genes_size"]
        self._genes_range = conf["genes_range"]
        self._r_mut = conf["mutation_probability"]

        self._number_of_genes = sum(self._genes_size)

        self.randomize()

    def randomize(self):
        self._genome = randint(low=0, high=2, size=self._number_of_genes, dtype=int)

    def binary_mutate(self):
        for i in range(len(self._genome)):
            if rand() < self._r_mut:
                self._genome[i] = 1 - self._genome[i]

    def set_fitness(self, val):
        self._fitness = val

    def get_fitness(self):
        return self._fitness

    def get_phenotype(self):
        phenotype = []
        actual_bit = 0
        for genes_size, genes_range in zip(self._genes_size, self._genes_range):
            binary = self._genome[actual_bit:genes_size + actual_bit]
            phenotype.append(self._binary_decode(scope=genes_range, binary=binary, size=genes_size))
            actual_bit = actual_bit + genes_size
        return phenotype

    def __str__(self):
        actual_bit = 0
        out = '['
        for gene_size in self._genes_size:
            out = out + str(self._genome[actual_bit:gene_size + actual_bit])
            actual_bit = actual_bit + gene_size
        out += ']'
        return out

    def _binary_decode(self, scope, binary, size):
        return scope[0] + ((scope[1] - scope[0]) / (pow(2, size) - 1)) * self._bin_to_dec(binary)

    @staticmethod
    def _bin_to_dec(binary):
        i = 0
        dec = 0
        for bit in binary:
            dec = dec + 2 ** i * bit
            i += 1
        return dec

    @staticmethod
    def _validate_config(configuration):
        v = Validator(schema)
        return v.validate(configuration), v.errors
