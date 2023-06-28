def isBalancedBrackets(brackets):
    l = len(brackets)
    if l == 0:   return True
    if(l%2==1): return False
    thisBrackets = BracketSeq(brackets)
    return thisBrackets.isBalanced()

class BracketSeq:
    def __init__(self, brackets) :
        self.brackets = brackets
        self.tracker = []
        self.tOS = -1
        self.pairs = {"(":")", "[":"]", "{":"}"}

    def isBalanced(self):
        brackets = self.brackets
        l = len(brackets)
        closingList = [")", "]", "}"]
        bracket = brackets[0]
        if bracket in closingList: return False
        self.push(bracket)
        for i in range(1, l):
            bracket = brackets[i]
            if((self.tOS==0)&(self.peek() in closingList)):    return False
            bracketPrev = self.peek()
            if(self.pairs[bracketPrev]==bracket):
                self.pop()
            else: self.push(bracket)
        return True

    def push(self, bracket):
        self.tracker.append(bracket)
        self.tOS += 1

    def peek(self):
        if(self.tOS>=0):    return self.tracker[self.tOS]

    def pop(self):
        if(self.tOS>=0):
            del self.tracker[self.tOS]
            self.tOS -= 1

brackets1 = ""
brackets2 = "("
brackets3 = ")("
brackets4 = "{()}"
brackets6 = "()"
print(isBalancedBrackets(brackets4)) 