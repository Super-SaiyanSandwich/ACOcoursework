import random
import matplotlib.pyplot as plt
import numpy

import Weight
import Ant
      

BPP = ""

""" def findBinsOfPath(path, weights):
    bins = [0]*b
    for i in range(k):
        bins[path[i][1]] += weights[i].getValue()
    return bins """   

def graphRepeatRun(fitnesses, numberOfAnts, evaporationRate, BPPName, trials):

    out = []
    minfit = float("inf")
    for x in fitnesses:
        x = numpy.array(x)
        if min(x) < minfit:
            minfit = min(x)
        out.append([minfit,max(x),(sum(x)/ numberOfAnts), min(x)])

    
    plt.plot(out)
    plt.title("Results of " + BPPName + " with " + str(numberOfAnts) + " ants and an evaporation rate of " + str(evaporationRate) + ".\nAveraged over " + str(trials) +" trials")
    plt.show()

def graphSingleRun(fitnesses, numberOfAnts, evaporationRate, BPPName):

    out = []
    minfit = float("inf")
    for x in fitnesses:
        x = numpy.array(x)
        if min(x[:,0]) < minfit:
            minfit = min(x[:,0])
        out.append([minfit,max(x[:,0]),(sum(x[:,0])/ numberOfAnts), min(x[:,0])])

    
    plt.plot(out)
    plt.title("Results of " + BPPName + "with " + str(numberOfAnts) + " ants and an evaporation rate of " + str(evaporationRate) + ".\nMinimum fitness found: " + str(minfit) + "")
    plt.show()

def BPP1(evaporationRate):
    numberOfWeights = 200
    numberOfBins = 10
 
    ###DECLRAING THE WEIGHTS FOR BPP1
    weights = []    

    for i in range(numberOfWeights):
        x  = Weight.Weight(random.randint(1,201),numberOfBins, evaporationRate)
        weights.append(x)

    return "BPP1", weights, numberOfBins, numberOfWeights

def BPP2(evaporationRate):
    numberOfWeights = 200
    numberOfBins = 50

    ###DECLRAING THE WEIGHTS FOR BPP1
    weights = []    

    for i in range(numberOfWeights):
        x  = Weight.Weight(((random.randint(1,201) * i)/2),numberOfBins, evaporationRate)
        weights.append(x)

    return "BPP2", weights, numberOfBins, numberOfWeights
    

def run(BPP, numberOfAnts, evaporationRate):

    ###SETTING BIN PACKING PROBLEM
    BPPName, weights, numberOfBins, numberOfWeights = BPP(evaporationRate) 
    
    ###CREATING p NUMBER OF ANTS
    ants = Ant.generateAnts(numberOfAnts, numberOfWeights, numberOfBins)

    ###SETTING MINIMUM FITNESS FOUND TO INFINITE
    minFit = float("inf")
    
    ###CREATING LIST FOR ALL FITNESSES (FOR GRAPHING LATER)
    fitnesses = []
    fitnessChecks = 0

    while True:

        genFit, minFit = Ant.generateGeneration(ants,weights,minFit)

        fitnesses.append(genFit)

        fitnessChecks += Ant.updateAnts(ants, weights)

        Weight.evaporateAll(weights)       
        
        if minFit == 0:
            break
        if fitnessChecks >= 10000:
            break    
    
    return fitnesses


def repeatRun(BPP, numberOfAnts, evaporationRate, trials):
    fitnessArr = []
    for i in range(trials):
        fitnessArr.append(run(BPP, numberOfAnts, evaporationRate))
    fitnessArr = numpy.array(fitnessArr)
    fitnessArr = numpy.mean(fitnessArr, axis= 0)

    return fitnessArr

graphRepeatRun(repeatRun(BPP1, 100, 0.9, 5),100,0.9,"BPP1",5)
graphRepeatRun(repeatRun(BPP1, 100, 0.3, 5),100,0.3,"BPP1",5)
graphRepeatRun(repeatRun(BPP1, 10, 0.3, 5),10,0.3,"BPP1",5)

graphRepeatRun(repeatRun(BPP2, 100, 0.9, 5),100,0.9,"BPP2",5)
graphRepeatRun(repeatRun(BPP2, 100, 0.3, 5),100,0.3,"BPP2",5)
graphRepeatRun(repeatRun(BPP2, 10, 0.9, 5),10,0.9,"BPP2",5)
graphRepeatRun(repeatRun(BPP2, 10, 0.3, 5),10,0.3,"BPP2",5) 
