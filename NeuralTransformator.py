import numpy as np
from CONFIG import *
import random

class Neuronio():
    def __init__(self, size):
        self.weights = np.random.random(size=size) * random.randint(-5, 5)


class Rede():
    def __init__(self, size, topology, weight=None):
        if weight is not None:
            self.weights = weight
        else:
            self.weights = np.random.random(size=size) * random.randint(-5, 5)
        self.layers = topology
        self.fitness = 0
    
    def reLU(self, x):
        return np.maximum(0, x)

    def feedforward(self, arrayData):
        temp

    def crossOver(self, otherRede):
        return Rede(self.weights.shape[0], self.layers, weight=(self.weights + otherRede.weights) / 2)

    def mutation(self):
        for i in range(len(self.weights)):
            if random.random() < MUTATIONRATE:
                self.weights[i] += random.randint(-5, 5) * np.random.random()

    def __lt__(self, other):
        return self.fitness < other.fitness
    
    def Fitness(self):
        pass