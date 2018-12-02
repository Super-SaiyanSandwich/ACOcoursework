import random
import matplotlib.pyplot as plt
import numpy
import pandas

import Weight
import Ant

      

###GRAPHS OUT A AVERAGE RUN FROM A REPEAT NUMBER OF RUNS
def graphRepeatRun(fitnesses, numberOfAnts, evaporationRate, BPPName, trials):

    out = []
    minfit = float("inf")
    for x in fitnesses:
        x = numpy.array(x)
        if min(x) < minfit:
            minfit = min(x)
        out.append([minfit,max(x),(sum(x)/ numberOfAnts), min(x)])

    plt.plot(out)
    plt.ylabel("Fitness")
    plt.xlabel("Generations")
    plt.title("Results of " + BPPName + " with " + str(numberOfAnts) + " ants and an evaporation rate of " + str(evaporationRate) + ".\nAveraged over " + str(trials) +" trials")
    
    plt.legend(["Minimum Average Fitness\nFound Thus Far","Largest Average Fitness", "Average Fitness", "Smallest Average Fitness"], fontsize = 'x-small',bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)

    plt.savefig(BPPName + str(numberOfAnts) + str(evaporationRate) + str(trials) + ".png",bbox_inches="tight")

### GRAPHS OUT THE RESULTS FROM A SINGLE RUN
def graphSingleRun(fitnesses, numberOfAnts, evaporationRate, BPPName):
    out = []
    minfit = float("inf")
    for x in fitnesses:
        x = numpy.array(x)
        if min(x[:,0]) < minfit:
            minfit = min(x[:,0])
        out.append([minfit,max(x[:,0]),(sum(x[:,0])/ numberOfAnts), min(x[:,0])])

    ###NOTE: MISSING LEGEND
    plt.plot(out)
    plt.title("Results of " + BPPName + "with " + str(numberOfAnts) + " ants and an evaporation rate of " + str(evaporationRate) + ".\nMinimum fitness found: " + str(minfit) + "")
    plt.show()

def BPP1(evaporationRate):
    ###BIN NUMBER AND WEIGHT NUMBER FOR PROBLEM
    numberOfWeights = 200
    numberOfBins = 10
 
    ###DECLRAING THE WEIGHTS FOR BPP1
    weights = []    

    for i in range(numberOfWeights):
        x  = Weight.Weight(random.randint(1,201),numberOfBins, evaporationRate)
        weights.append(x)

    return "BPP1", weights, numberOfBins, numberOfWeights


def BPP2(evaporationRate):
    ###BIN NUMBER AND WEIGHT NUMBER FOR PROBLEM
    numberOfWeights = 200
    numberOfBins = 50

    ###DECLRAING THE WEIGHTS FOR BPP1
    weights = []    

    for i in range(numberOfWeights):
        x  = Weight.Weight(((random.randint(1,201) * i)/2),numberOfBins, evaporationRate)
        weights.append(x)

    return "BPP2", weights, numberOfBins, numberOfWeights
    
###MAIN ACO FUNCTION
def run(BPP, numberOfAnts, evaporationRate):

    ###SETTING BIN PACKING PROBLEM
    BPPName, weights, numberOfBins, numberOfWeights = BPP(evaporationRate) 
    
    ###CREATING A NUMBER OF ANTS
    ants = Ant.generateAnts(numberOfAnts, numberOfWeights, numberOfBins)

    ###SETTING MINIMUM FITNESS FOUND TO INFINITE
    minFit = float("inf")
    
    ###CREATING LIST FOR ALL FITNESSES (FOR GRAPHING LATER)
    fitnesses = []
    fitnessChecks = 0

    while True:

        genFit, minFit = Ant.generateGeneration(ants,weights,minFit)
        genFit = numpy.sort(genFit)

        fitnesses.append(genFit)

        fitnessChecks += Ant.updateAnts(ants, weights)

        Weight.evaporateAll(weights)       
        
        ###CHECKS WHETHER TERMINATION CONDITION HAS BEEN MET OR NOT
        if fitnessChecks >= 10000:
            break    
    
    return fitnesses


###MAIN ACO FUNCTION, MINFIT VARIANT
def minRun(BPP, numberOfAnts, evaporationRate):

    ###SETTING BIN PACKING PROBLEM
    BPPName, weights, numberOfBins, numberOfWeights = BPP(evaporationRate) 
    
    ###CREATING A NUMBER OF ANTS
    ants = Ant.generateAnts(numberOfAnts, numberOfWeights, numberOfBins)

    ###SETTING MINIMUM FITNESS FOUND TO INFINITE
    minFit = float("inf")
    
    fitnessChecks = 0

    while True:

        genFit, minFit = Ant.generateGeneration(ants,weights,minFit)

        fitnessChecks += Ant.updateAnts(ants, weights)

        Weight.evaporateAll(weights)       
        
        ###CHECKS WHETHER TERMINATION CONDITION HAS BEEN MET OR NOT
        if fitnessChecks >= 10000:
            break    
    
    return minFit



###RUNS THE ACO ALGORITHM MULTIPLE TIMES
def repeatRun(BPP, numberOfAnts, evaporationRate, trials):
    fitnessArr = []
    for i in range(trials):
        fitnessArr.append(run(BPP, numberOfAnts, evaporationRate))
    fitnessArr = numpy.array(fitnessArr)
    fitnessArr = numpy.mean(fitnessArr, axis= 0)

    print("Repeat trials of " + str(numberOfAnts) + " " + str(evaporationRate) + " " + str(trials) + "complete")
    return fitnessArr



###RUNS THE ACO ALGORITHM MULTIPLE TIMES ONLY CARING ABOUT MINIMUM FIT
def repeatMin(BPP, numberOfAnts, evaporationRate, trials):
    minFitAv = 0
    for i in range(trials):
        minFitAv += minRun(BPP, numberOfAnts, evaporationRate)
    
    return minFitAv/trials

### EXPERIMENTS ASKED FOR BY THE COURSEWORK
""" print("Beginning")
graphRepeatRun(repeatRun(BPP1, 100, 0.9, 10),100,0.9,"BPP1",10)
graphRepeatRun(repeatRun(BPP1, 100, 0.4, 10),100,0.4,"BPP1",10)
graphRepeatRun(repeatRun(BPP1, 10, 0.9, 10),10,0.9,"BPP1",10)
graphRepeatRun(repeatRun(BPP1, 10, 0.4, 10),10,0.4,"BPP1",10)

graphRepeatRun(repeatRun(BPP2, 100, 0.9, 10),100,0.9,"BPP2",10)
graphRepeatRun(repeatRun(BPP2, 100, 0.4, 10),100,0.4,"BPP2",10)
graphRepeatRun(repeatRun(BPP2, 10, 0.9, 10),10,0.9,"BPP2",10)
graphRepeatRun(repeatRun(BPP2, 10, 0.4, 10),10,0.4,"BPP2",10) """

###FOR FURTHER WORK SECTION: OPTIMAL PAIRINGS
""" out = numpy.zeros((19,13))
antNums = list(range(10,105,5))
evapRates = numpy.array(range(30,91,5)) / 100
for i in range(19): 
    antNum = 10 + (i * 5)
    for j in range(13):
        evapRate = 0.3 + (j*0.05)
        out[i,j] = repeatMin(BPP1, antNum, evapRate, 5)
        print(str(antNums[i]) + " , " + str(evapRates[j]))
a = pandas.DataFrame(out, antNums, evapRates)
print(a) """
