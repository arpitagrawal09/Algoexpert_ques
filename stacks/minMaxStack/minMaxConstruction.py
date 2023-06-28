# Feel free to add new properties and methods to the class.
class MinMaxStack:

    def __init__(self):
        self.stack = []
        self.top = 0
        self.min = 10000000000
        self.max = -1
        
    def peek(self):
        # Write your code here.
        if(self.top>0):
            return self.stack[self.top-1]
       #else:   return None

    def pop(self):
        # Write your code here.
        top = self.top
        removed = -1
        if(top>0):
            removed = self.stack.pop()
            self.top -= 1
        #top = self.top
        if(top>0):
            self.min = min(self.min, self.stack[self.top-1])
            self.max = max(self.max, self.stack[self.top-1])
        if(removed>0):
            return removed
    
    def push(self, number):
        # Write your code here.
        #self.stack.insert(self.top, number)
        self.stack.append(number)
        self.top+=1
        top = self.top
        if(top>0):
            self.min = min(self.min, self.stack[self.top-1])
            self.max = max(self.max, self.stack[self.top-1])        

    def getMin(self):
        # Write your code here.
        return self.min

    def getMax(self):
        # Write your code here.
        return self.max

stack1 = MinMaxStack()
print(stack1.peek())
print(stack1.pop())
print(stack1.getMax())
print(stack1.getMin())

print(stack1.push(37))
print(stack1.peek())
print(stack1.getMax())
print(stack1.getMin())

stack1.push(93532)
stack1.pop()
stack1.peek()
