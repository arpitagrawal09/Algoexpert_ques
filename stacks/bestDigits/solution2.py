#Submission at algoexpert. Solution 2. Accepted 

def bestDigits(number, numDigits):
    if numDigits < 0: return -1
    if numDigits == 0 : return number 
    if numDigits > len(number) : return -1
    thisLargest = Operator(number, numDigits)
    return thisLargest.condense()

class Operator:
    def __init__(self, num, removeDig):
        self.num = num
        self.remove = removeDig
        self.stack = []
        self.tOS = -1
        self.string = ""

    def condense(self):
        self.push(int(self.num[0]))
        i = 1
        while(i<len(self.num)):
            dProspect = int(self.num[i])
            dLast = self.peek()
            if dLast == -1 : 
                self.push(dProspect)
                i+=1
            elif((self.remove!=0)&(dProspect>dLast)):
                self.pop()
            else:
                self.push(dProspect)
                i += 1
        if((i==len(self.num))&(self.remove>0)):
            for j in range(self.remove):
                self.pop()
        self.getString()
        return self.string

    def getString(self):
        for i in range(len(self.stack)):
            self.string += str(self.stack[i])

    def push(self, digit):
        self.stack.append(digit)
        self.tOS += 1

    def pop(self):
        if self.tOS == -1: return -1
        del self.stack[self.tOS]
        self.tOS -= 1
        self.remove-=1

    def peek(self):
        if self.tOS == -1: return -1
        return self.stack[self.tOS]

