def balancedBrackets(string):
    l = len(string)
    if l == 0:   return True
    #if(l%2==1): return False
    thisBrackets = BracketSeq(string)
    return thisBrackets.isBalanced()


class BracketSeq:
    def __init__(self, brackets) :
        self.brackets = brackets
        self.tracker = []
        self.tOS = -1
        self.bracketPairs = {"(":")", "[":"]", "{":"}"}

    def cleanBrackets(self):
        reducedStr = ""
        literals = []
        for literal in self.bracketPairs:
            literals.append(literal)
            literals.append(self.bracketPairs[literal])
        for literal in self.brackets:
            if literal in literals:
                reducedStr += literal
        self.brackets = reducedStr
        
    def isBalanced(self):
        self.cleanBrackets()
        brackets = self.brackets
        l = len(brackets)
        print(l)
        if l%2 == 1: return False
        closingList = []
        for openingBracket in self.bracketPairs:
            closingList.append(self.bracketPairs[openingBracket])
        closingBrackets = set(closingList)
        for i in range(0, l):
            bracket = self.brackets[i]
            #if(i == 9): print(bracket)
            if(self.tOS == -1) :
                if(bracket in closingBrackets): return False
                else: self.push(bracket)
            else: 
                bracketPrev = self.peek()
                if(bracketPrev in closingBrackets): return False
                if(self.bracketPairs[bracketPrev]==bracket):
                    self.pop()
                else: self.push(bracket)
            #if(i==8): print(self.tracker)
            #print(self.tracker)
        if self.tOS == -1 : return True
        else: return False

    def push(self, bracket):
        self.tracker.append(bracket)
        self.tOS += 1

    def peek(self):
        if(self.tOS>=0):    return self.tracker[self.tOS]
        return -1 

    def pop(self):
        if(self.tOS>=0):
            del self.tracker[self.tOS]
            self.tOS -= 1

testCase1 = "([])(){}(())()()"
testCase12 = "{[[[[({(}))]]]]}"

print(balancedBrackets(testCase12))