#Submission at Algoexpert. Solution 1. Rejected

def bestDigits(number, numDigits):

    thisNum = NumManipulate(number, numDigits)
    numShortened = thisNum.getShortenedNum()
    return numShortened

class NumManipulate:

    def __init__(self, numGot, nD):
        self.numGot = numGot
        self.nD = nD
        self.numGive = []
        self.tOS = -1
    
    def peek(self):
        if self.tOS == -1 : return -1
        return self.numGive[self.tOS ]
        
    def pop(self):
        if self.tOS == -1: return -1
        digit = self.numGive[self.tOS]
        del self.numGive[self.tOS]
        self.tOS -= 1

    def push(self, digitNow):
        self.numGive.append(digitNow)
        self.tOS += 1

    def getShortenedNum(self):
        if len(self.numGot) == 0 : return ""
        numGot = self.numGot
        nD = self.nD
        self.numGive.append(int(numGot[0]))
        for i in range(1, len(numGot)):
            digitNow = int(numGot[i])
            if nD == 0: self.push(digitNow)
            else:
                if digitNow <= self.peek():
                    self.push(digitNow)
                else: 
                    self.pop()
                    self.push(digitNow)
                    nD -= 1
        numFinal = ""
        for i in range(0, len(self.numGive)):
            char = str(self.numGive[i])
            numFinal += char 
        return numFinal 
        

