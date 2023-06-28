# First two out of the 4 test cases passed 
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
    
    def pop(self):
        # Write your code here.
        top = self.top
        removed = -1
        if(top>0):
            removed = self.stack.pop()
            self.top -= 1
        top = self.top
        if(top>0):
            max = -1
            min = 10000000000            
            for i in range(top):
                element = self.stack[i]
                if(element>max): max = element
                if(element<min): min = element
            self.max = max
            self.min = min 
            #self.min = min(self.min, self.stack[top-1])
            #self.max = max(self.max, self.stack[top-1])
        if(top==0):
            self.max = -1
            self.min = 1000000000
        if(removed>0):
            return removed
    
    def push(self, number):
        #self.stack.insert(self.topOfStack, number)
        self.stack.append(number)
        self.top+=1
        top = self.top
        if(top>0):
            self.min = min(self.min, number)
            self.max = max(self.max, number)        

    def getMin(self):
        # Write your code here.
        return self.min

    def getMax(self):
        # Write your code here.
        return self.max

stack1 = MinMaxStack()

#SET 1 
"""print(stack1.push(5))
print(stack1.getMin())
print(stack1.getMax())
print(stack1.peek())

print(stack1.push(7))
print(stack1.getMin())
print(stack1.getMax())
print(stack1.peek())

print(stack1.push(2))
print(stack1.getMin())
print(stack1.getMax())
print(stack1.peek())

print(stack1.pop())
print(stack1.pop())
print(stack1.getMin())
print(stack1.getMax())
print(stack1.peek())"""

print(stack1.getMin())
print(stack1.getMax())
print(stack1.peek())
print(stack1.pop())

"""print(stack1.push(5))
print(stack1.getMin())
print(stack1.getMax())
print(stack1.peek())

print(stack1.push(7))
print(stack1.getMin())
print(stack1.getMax())
print(stack1.peek())

print(stack1.push(2))
print(stack1.getMin())
print(stack1.getMax())
print(stack1.peek())

print(stack1.pop())
print(stack1.pop())
print(stack1.getMin())
print(stack1.getMax())
print(stack1.peek())"""