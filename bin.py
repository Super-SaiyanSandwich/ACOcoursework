import random

class Bin:
    def __init__(self, binNum, evapRate, totalBins):
        self.totalBins = totalBins
        self.pheromones = [random.uniform(0,1)] * self.totalBins
        self.binNum = binNum
        self.evapRate = evapRate
        

    def chooseRandBin(self):
        x = sum(self.pheromones)
        r = random.uniform(0,x)
        s = 0
        for i in range(self.totalBins):
            s += self.pheromones[i]
            if s >= r:
                return i
        return self.totalBins - 1

    def evaporate(self):
        for phero in self.pheromones:
            phero *= self.evapRate

    def increase(self, path, value):
        self.pheromones[path] += value