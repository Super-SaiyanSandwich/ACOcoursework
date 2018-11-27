import bin

class Weight:
    def __init__(self, value, totalBins, evapRate):
        self.value = value
        self.bins = []
        for i in range(totalBins):
            x = bin.Bin(i,evapRate,totalBins)
            self.bins.append(x)

    def getValue(self):
        return self.value

    
    def chooseRandBin(self, path):
        return self.bins[path].chooseRandBin()

    def chooseInitialBin(self):
        return self.bins[0].chooseRandBin()

    def evaporate(self):
        for bini in self.bins:
            bini.evaporate()
    
    def increase(self, bini, path, value):
        self.bins[bini].increase(path, value)