###ANT OBJECT FOR THE ACO ALGORITHM
class Ant:
    ###CREATE AN ANT OBJECT
    def __init__(self, numberWeights, totalBins):
        self.numberWeights = numberWeights
        self.totalBins = totalBins
        self.path = [0] * numberWeights
        self.binValue = [0]
        self.fitness = float("inf")

    ###GENERATE A PATH FOR THE ANT
    def generatePath(self, weights):
        self.binValue = [0] * self.totalBins

        x = weights[self.numberWeights - 1].chooseInitialBin()
        self.path[0] = x
        self.binValue[x] += weights[0].getValue()

        for i in range(self.numberWeights - 1):
            x = weights[i].chooseRandBin(self.path[i])
            self.path[i+1] = x
            self.binValue[x] += weights[i+1].getValue()

    ###CALCULATES THE FITNESS OF THE PATH
    def setFitness(self):
        self.fitness = max(self.binValue) - min(self.binValue)
        return self.fitness

    ###UPDATES THE PHEROMONES OF THE PATHS
    def updatePheromone(self, weights):
        self.setFitness()        
        weights[self.numberWeights - 1].increase(0,self.path[0], 100 / self.fitness)
        for i in range(self.numberWeights - 1):            
            weights[i].increase(self.path[i], self.path[i+1], 100 / self.fitness)

###GENERATES A SET OF ANTS
def generateAnts(antNumber,weightNumber,binNumber):
    ants = []
    for i in range(antNumber):
        x = Ant(weightNumber,binNumber)
        ants.append(x)
    return ants

###UPDATES PHEROMONES FOR A SET OF ANTS
def updateAnts(ants, weights):
    for ant in ants:
        ant.updatePheromone(weights)
    return len(ants)

###GENERATES A GENERATION OF PATHS FOR A SET OF ANTS
def generateGeneration(ants, weights, minFit):
    genFit = []

    for ant in ants:
        ant.generatePath(weights)

        x = ant.setFitness()
        genFit.append(x)

        if x < minFit:
            minFit = x
    return genFit, minFit