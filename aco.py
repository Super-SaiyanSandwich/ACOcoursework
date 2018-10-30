import random
import matplotlib.pyplot as plt

import cProfile

import time

k = 200 # Number of Weights
b = 10 # Bin Number
p = 100 # Ant Number
e = 0.4 # Evaporation Rate
t = 100 # Max Number of Iterations

class Weight:
    def __init__(self, value):
        self.value = value
        self.bins = []
        for i in range(b):
            x = Bin(i)
            self.bins.append(x)

    def getValue(self):
        return self.value

    
    def chooseRandBin(self, path):
        return self.bins[path].chooseRandBin()

    def chooseInitialBin(self):
        return self.bins[0].chooseRandBin()

    def evaporate(self):
        for bin in self.bins:
            bin.evaporate()
    
    def increase(self, bin, path, value):
        self.bins[bin].increase(path, value)


class Bin:
    def __init__(self, binNum):
        self.pheromones = [random.uniform(0,1)] * b
        self.binNum = binNum

    def chooseRandBin(self):
        x = sum(self.pheromones)
        r = random.uniform(0,x)
        s = 0
        for i in range(b):
            s += self.pheromones[i]
            if s >= r:
                return i
        return b - 1

    def evaporate(self):
        for phero in self.pheromones:
            phero *= e

    def increase(self, path, value):
        self.pheromones[path] += value

class Ant:
    def __init__(self):
        self.path = [(0,0)] * k
        self.binValue = [0] * b
        self.fitness = float("inf")

    def generatePath(self, weights):
        self.binValue = [0] * b

        x = weights[k-1].chooseInitialBin()
        self.path[0] = x
        self.binValue[x] += weights[0].getValue()

        for i in range(k-1):
            x = weights[i].chooseRandBin(self.path[i])
            self.path[i+1] = x
            self.binValue[x] += weights[i+1].getValue()

    def setFitness(self):
        self.fitness = max(self.binValue) - min(self.binValue)
        return self.fitness

    def updatePheromone(self, weights):
        x = self.setFitness()
        weights[k-1].increase(0,self.path[0], 10000 / x**2)
        #weights[k-1].increase(0,self.path[0], 100 / x)
        for i in range(k-1):            
            if x == 0:
                weights[i].increase(self.path[i+1], self.path[i], float("inf"))
            else:
                weights[i].increase(self.path[i+1], self.path[i], 10000 / x**2)
                #weights[i].increase(self.path[i], 100 / x)
        


""" def findBinsOfPath(path, weights):
    bins = [0]*b
    for i in range(k):
        bins[path[i][1]] += weights[i].getValue()
    return bins """


def main():
    weights = []

    #BPP1
    """ for i in range(k):
        x  = Weight(random.randint(1,201))
        weights.append(x) """

    #BPP2
    for i in range(k):
        x  = Weight((random.randint(1,201) * i)/2)
        weights.append(x)

    ants = []

    for i in range(p):
        x = Ant()
        ants.append(x)

    minFit = float("inf")
    #minPath = []

    fitnesses = []

    for i in range(t):
        genFit = []

        for ant in ants:

            ant.generatePath(weights)

            x = ant.fitness
            genFit.append(x)
            if x < minFit:
                minFit = x
                minPath = ant.path.copy()
                print(i)
                print(minFit)
                #print(findBinsOfPath(minPath,weights))
        for ant in ants:
            ant.updatePheromone(weights)
        for weight in weights:
            weight.evaporate()
        fitnesses.append(genFit)
        if minFit == 0:
            break


    out = []

    minfit = float("inf")
    for x in fitnesses:
        if min(x) < minfit:
            minfit = min(x)
        out.append([minfit,max(x),(sum(x)/p)])

    print("Out")

    plt.plot(out)
    plt.show()

main()