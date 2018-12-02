import random
import matplotlib.pyplot as plt
import numpy
import pandas



import WeightH
import AntH
      

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

### ALTERNATE FOR HEURISTIC BASED TESTS
def BPP1H(evaporationRate):
    ###BIN NUMBER AND WEIGHT NUMBER FOR PROBLEM
    numberOfWeights = 200
    numberOfBins = 10
 
    ###DECLRAING THE WEIGHTS FOR BPP1
    weights = []    

    for i in range(numberOfWeights):
        x  = WeightH.Weight(random.randint(1,201),numberOfBins, evaporationRate)
        weights.append(x)

    return "BPP1", weights, numberOfBins, numberOfWeights


###MAIN ACO FUNCTION: ALTERNATE FOR HEURISTIC TESTS
def runH(BPP, numberOfAnts, evaporationRate):

    ###SETTING BIN PACKING PROBLEM
    BPPName, weights, numberOfBins, numberOfWeights = BPP(evaporationRate) 
    
    ###CREATING A NUMBER OF ANTS
    ants = AntH.generateAnts(numberOfAnts, numberOfWeights, numberOfBins)

    ###SETTING MINIMUM FITNESS FOUND TO INFINITE
    minFit = float("inf")
    
    ###CREATING LIST FOR ALL FITNESSES (FOR GRAPHING LATER)
    fitnesses = []
    fitnessChecks = 0

    while True:

        genFit, minFit = AntH.generateGeneration(ants,weights,minFit)
        genFit = numpy.sort(genFit)

        fitnesses.append(genFit)

        fitnessChecks += AntH.updateAnts(ants, weights)

        WeightH.evaporateAll(weights)       
        
        ###CHECKS WHETHER TERMINATION CONDITION HAS BEEN MET OR NOT
        if fitnessChecks >= 10000:
            break    
    
    return fitnesses


###RUNS THE ACO ALGORITHM MULTIPLE TIMES
def repeatRunH(BPP, numberOfAnts, evaporationRate, trials):
    fitnessArr = []
    for i in range(trials):
        fitnessArr.append(runH(BPP, numberOfAnts, evaporationRate))
    fitnessArr = numpy.array(fitnessArr)
    fitnessArr = numpy.mean(fitnessArr, axis= 0)

    print("Repeat trials of " + str(numberOfAnts) + " " + str(evaporationRate) + " " + str(trials) + "complete")
    return fitnessArr



###FOR FURTHER WORK SECTION: HEURISTCS
graphRepeatRun(repeatRunH(BPP1H, 10, 0.9, 10),10,0.9,"BPP1, with Altered Heuristics, ",10)