import random
import matplotlib.pyplot as plt
import numpy

import Weight
import Ant

k = 50 # Number of Weights
b = 10 # Bin Number
p = 100 # Ant Number
e = 0.3 # Evaporation Rate
t = 100 # Max Number of Iteration        


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
        x  = weightObj.Weight(random.randint(1,201))
        weights.append(x) """

    #BPP2
    for i in range(k):
        x  = Weight.Weight(((random.randint(1,201) * i)/2), b, e)
        weights.append(x)

    
    ###CREATING p NUMBER OF ANTS
    ants = []
    for i in range(p):
        x = Ant.Ant(k,b)
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

        for i in range(p):
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

main()