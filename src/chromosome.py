import numpy as np

class Chromosome():

    def __init__(self, number_of_alles:int, allel_len:int):
        self.fitness = 0
        self.number_of_allels = number_of_alles
        self.allel_len = allel_len
        self.fenotype = np.array((self.number_of_allels,self.allel_len))
        self.allowed_allels= (0,0)
        
    def generate(self):
        
        self.fenotype = np.random.randint(low=self.allowed_allels[0], high=self.allowed_allels[-1]+1, size=(self.number_of_allels,self.allel_len), dtype=int)      
        
    def __str__(self):
        string_allel = ''
        for allel in self.fenotype:
            str = str + str(allel) + '\n'
        return string_allel
        
        

class BinChromosome(Chromosome):

    def __init__(self, number_of_alles, allel_len):
        super().__init__(number_of_alles, allel_len)
        
        self.allowed_allels = (0, 1)
        
    
class GrayChromosome(BinChromosome):
    def __init__(self, number_of_alles, allel_len):
        super().__init__(number_of_alles, allel_len)
        
    def generate():
        pass
        
class LogChromosome(BinChromosome):

    def __init__(self, number_of_alles, allel_len):
        super().__init__(number_of_alles, allel_len)
    


class TriaChromosome(Chromosome):
    
    def __init__(self, number_of_alles, allel_len):
        super().__init__(number_of_alles, allel_len)
        
        self.allowed_allels = (-1, 0, 1)
        
        
class IntChromosome(Chromosome):
    pass
    
class LayerChromosome(Chromosome):
    pass
        
               
        
        