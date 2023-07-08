#Submission at Algoexpert. Solution 1. Accepted 

def sunsetViews(buildings, direction):
    stack1 = buildingStack(buildings, direction)
    return stack1.visible()

class buildingStack:
    def __init__(self, buildings, direction):
        self.buildings = buildings
        self.direction = direction
        self.tallest = -1
        self.visibleGroup = []
        self.l = len(self.buildings)
        if(direction == "EAST"): self.tOS = self.l -1
        else: self.tOS = 0
    
    def pop(self):
        self.tallest = max(self.buildings[self.tOS], self.tallest)
        #del self.buildings[self.tOS]
        if(self.direction == "EAST"): self.tOS -= 1
        else: self.tOS += 1

    def visible(self):
        if(self.direction == "EAST"): i = self.l
        else: i = 0
        while((self.tOS>=0)&(self.tOS<self.l)):
            if(self.buildings[self.tOS]>self.tallest): 
                if(self.direction == "EAST") : 
                    self.visibleGroup.append(self.tOS)
                    i -= 1
                else: self.visibleGroup.append(self.tOS)
            self.pop()
        self.visibleGroup.sort()
        return self.visibleGroup



    