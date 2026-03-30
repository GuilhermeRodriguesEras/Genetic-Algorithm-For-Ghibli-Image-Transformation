import numpy as np
from CONFIG import *
import random

class Rede():
    def __init__(self, size, rng, topology):
        self.weights = rng.random(size=size)
        self.layers = topology
        self.rng = rng
    
    def feedforward(self, arrayData):
        pass

    def crossOver(self, otherRede):
        self.weights = (self.weights + otherRede.weights) / 2

    def mutation(self):
        for i in range(len(self.weights)):
            if self.rng.random() < MUTATIONRATE:
                self.weights[i] += random.randint(0,1)*(-1)*self.rng.random()