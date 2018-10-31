import random
import matplotlib.pyplot as plt
import numpy

import cProfile

import time

k = 50 # Number of Weights
b = 10 # Bin Number
p = 100 # Ant Number
e = 0.9 # Evaporation Rate
t = 1000 # Max Number of Iterations
r = 0.3 # Percentage of Ants that update thier pheromones

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
        self.path = [0] * k
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
        #weights[k-1].increase(0,self.path[0], 10000 / x**2)
        weights[k-1].increase(0,self.path[0], 200000 / x)
        for i in range(k-1):            
            weights[i].increase(self.path[i+1], self.path[i], 200000 / x)
        


""" def findBinsOfPath(path, weights):
    bins = [0]*b
    for i in range(k):
        bins[path[i][1]] += weights[i].getValue()
    return bins """
    

def main():

    ###DECLRAING THE WEIGHTS
    weights = []

    #BPP1
    """ for i in range(k):
        x  = Weight(random.randint(1,201))
        weights.append(x) """

    #BPP2
    for i in range(k):
        x  = Weight((random.randint(1,201) * i)/2)
        weights.append(x)

    
    ###CREATING p NUMBER OF ANTS
    ants = []
    for i in range(p):
        x = Ant()
        ants.append(x)

    ###SETTING MINIMUM FITNESS FOUND TO INFINITE
    minFit = float("inf")
    
    ###CREATING LIST FOR ALL FITNESSES (FOR GRAPHING LATER)
    fitnesses = []


    for i in range(t):

        genFit = []

        for ant in ants:
            ant.generatePath(weights)

            x = ant.setFitness()
            genFit.append([x, ant])

            if x < minFit:
                minFit = x
                print(i)
                print(minFit)
                #print(findBinsOfPath(minPath,weights))

        fitnesses.append(genFit.copy())

        genFit = numpy.array(genFit)
        genFit = genFit[genFit[:,0].argsort()]

        for i in range(int(p * r)):
            genFit[i,1].updatePheromone(weights)


        for weight in weights:
            weight.evaporate()
        
        if minFit == 0:
            break


    out = []

    minfit = float("inf")
    for x in fitnesses:
        x = numpy.array(x)
        if min(x[:,0]) < minfit:
            minfit = min(x[:,0])
        out.append([minfit,max(x[:,0]),(sum(x[:,0])/p), min(x[:,0])])

    print("Out")

    plt.plot(out)
    plt.show()


def test():
    ###DECLRAING THE WEIGHTS
    weights = []

    for i in range(100):
        x  = Weight(i)
        weights.append(x)

    
    ###CREATING p NUMBER OF ANTS
    ants = []
    for i in range(p):
        x = Ant()
        ants.append(x)

    ###SETTING MINIMUM FITNESS FOUND TO INFINITE
    minFit = float("inf")
    
    ###CREATING LIST FOR ALL FITNESSES (FOR GRAPHING LATER)
    fitnesses = []


    for i in range(t):

        genFit = []

        for ant in ants:
            ant.generatePath(weights)

            x = ant.setFitness()
            genFit.append([x, ant])

            if x < minFit:
                minFit = x
                print(i)
                print(minFit)
                #print(findBinsOfPath(minPath,weights))

        fitnesses.append(genFit.copy())

        genFit = numpy.array(genFit)
        genFit = genFit[genFit[:,0].argsort()]

        for i in range(int(p * r)):
            genFit[i,1].updatePheromone(weights)


        for weight in weights:
            weight.evaporate()
        
        if minFit == 0:
            break


    out = []

    minfit = float("inf")
    for x in fitnesses:
        x = numpy.array(x)
        if min(x[:,0]) < minfit:
            minfit = min(x[:,0])
        out.append([minfit,max(x[:,0]),(sum(x[:,0])/p), min(x[:,0])])

    print("Out")

    plt.plot(out)
    plt.show()

test()