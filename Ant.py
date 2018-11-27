
class Ant:
    def __init__(self, numberWeights, totalBins):
        self.numberWeights = numberWeights
        self.totalBins = totalBins
        self.path = [0] * numberWeights
        self.binValue = [0] * totalBins
        self.fitness = float("inf")

    def generatePath(self, weights):
        self.binValue = [0] * self.totalBins

        x = weights[self.numberWeights - 1].chooseInitialBin()
        self.path[0] = x
        self.binValue[x] += weights[0].getValue()

        for i in range(self.numberWeights - 1):
            x = weights[i].chooseRandBin(self.path[i])
            self.path[i+1] = x
            self.binValue[x] += weights[i+1].getValue()

    def setFitness(self):
        self.fitness = max(self.binValue) - min(self.binValue)
        return self.fitness

    def updatePheromone(self, weights):
        self.setFitness()
        #weights[k-1].increase(0,self.path[0], 10000 / x**2)
        weights[self.numberWeights - 1].increase(0,self.path[0], 100 / self.fitness)
        for i in range(self.numberWeights - 1):            
            weights[i].increase(self.path[i+1], self.path[i], 100 / self.fitness)