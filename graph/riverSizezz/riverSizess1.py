def riverSizes(matrix):
    thisTopology = Topology(matrix)
    return thisTopology.getSizes()

class Topology:
    def __init__(self, booleanTopology):
        self.booleanTopology = booleanTopology
        self.sizes = []
        self.graphTopology = []
        self.traversed = []

    def setTraversed(self):
        for i in len(self.booleanTopology):
            self.traversed.append([])
            for j in len(self.booleanTopology[0]):
                self.traversed[i].append(False)
    
    def setGraphTopology(self):
        for i in len(self.booleanTopology):
            self.graphTopology.append([])
            for j in len(self.booleanTopology[i]):
                value = self.booleanTopology[i][j]
                node = Location(value, i, j)
                self.graphTopology[i].append(node)

        for i in len(self.booleanTopology):
            for j in len(self.booleanTopology[i]):
                node = self.graphTopology[i][j]
                if i-1 >= 0: 
                    left = self.graphTopology[i-1][j]
                    node.neighbours.append(left)
                if j+1 <= len(self.booleanTopology[0]): 
                    down = self.graphTopology[i][j+1]
                    node.neighbours.append(down)
                if i+1 <= len(self.booleanTopology): 
                    right = self.graphTopology[i+1][j]
                    node.neighbours.append(right)
                if j-1 >= 0: 
                    up = self.graphTopology[i][j-1]
                    node.neighbours.append(up)

    def getSizes(self, node, size=0):
        if node.value == 0:
            for neighbour in node.neighbours:
                if neighbour is not None:
                    self.getSizes(neighbour, 0)
            self.sizes.append(size)
        else:
            size += 1
            for neighbour in node.neighbours:
                if neighbour is not None:
                    self.getSizes(neighbour, size)
            self.sizes.append(size)            

        for i in range(len(self.graphTopology)):
        i = 0
        j = 0
        sizes = []
        size = 0
        rows = len(self.booleanTopology)
        cols = len(self.booleanTopology[0])
        while((i>=0)&(i<=rows-1)&(j<=cols-1)&(j>=0)):
            self.traversed[i][j]=True
            presence = self.booleanTopology[i][j]    
            if presence ==0 : 

class Location:
    def __init__(self, value, row, col):
        self.value = value
        self.row = row
        self.col = col 
        self.neighbours = []

