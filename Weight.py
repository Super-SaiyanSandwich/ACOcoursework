import bin

###USED FOR THE GENERATION OF THE CONSTRUCTION GRAPH
class Weight:
    def __init__(self, value, totalBins, evapRate):
        self.value = value
        self.bins = []
        for i in range(totalBins):
            x = bin.Bin(i,evapRate,totalBins)
            self.bins.append(x)

    def getValue(self):
        return self.value

    ###RETURN SPECIFIC BIN'S PHEROMONES
    def getBinPheromone(self, bini):
        return self.bins[bini].getPheromones()

    ###RETURN ALL BINS' PHEROMONES
    def getPheromones(self):
        out = []
        for bini in self.bins:
            out.append(bini.getPheromones())
        return out

    ###CHOOSE A RANDOM BIN TO GO TO BASED ON THE PREVIOUS SELECTED
    def chooseRandBin(self, path):
        return self.bins[path].chooseRandBin()

    ###RATHER THAN HAVE A UNIQUE OBJECT FOR THE INTIAL STEP OF THE CONSTRUCTION GRAPH
    ###USES THE END WEIGHT THAT LEADS NOWHERE AS A REPLACEMENT OBJECT. SAVES SPACE
    def chooseInitialBin(self):
        return self.bins[0].chooseRandBin()

    def evaporate(self):
        for bini in self.bins:
            bini.evaporate()
    
    def increase(self, bini, path, value):
        self.bins[bini].increase(path, value)

def evaporateAll(weights):
    for weight in weights:
        weight.evaporate()  