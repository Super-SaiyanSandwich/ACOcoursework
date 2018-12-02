import random
import scipy.stats as ss
import numpy

###USED FOR THE GENERATION OF THE CONSTRUCTION GRAPH
class Bin:
    ###CREATE A BIN OBJECT
    def __init__(self, binNum, evapRate, totalBins):
        self.totalBins = totalBins
        self.pheromones = [0] * self.totalBins
        for i in range(self.totalBins):
            self.pheromones[i] = random.uniform(0,1)
        self.binNum = binNum
        self.evapRate = evapRate

    def getPheromones(self):
        return self.pheromones

    ###SELECT RANDOM BIN IN NEXT SECTION OF CONSTRUCTION GRAPH
    def chooseRandBin(self, bins, value):
        bins = len(bins) - ss.rankdata(bins) + 1
        a = numpy.array(self.pheromones) * bins
        x = sum(a)
        r = random.uniform(0,x)
        s = 0
        for i in range(self.totalBins):
            s += a[i]
            if s >= r:
                return i
        return self.totalBins - 1

    def evaporate(self):
        for i in range(self.totalBins):
            self.pheromones[i] *= self.evapRate

    def increase(self, path, value):
        self.pheromones[path] += value