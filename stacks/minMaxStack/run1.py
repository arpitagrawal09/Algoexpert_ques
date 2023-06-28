# All the four test cases failed with this code. I am yet to know why it happens so
# I have tried to match the the expected output with mine. I don't understand because
#these outputs seem to match. They are stored in a Google docs 

#I must have failed somewhere in the popping. Correction also doesn't pass the 
#test cases. This is why I transfer the output to run 2

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
            self.min = min(self.min, self.stack[top-1])
            self.max = max(self.max, self.stack[top-1])
        if(removed>0):
            return removed
    
    def push(self, number):
        #self.stack.insert(self.topOfStack, number)
        self.stack.append(number)
        self.top+=1
        top = self.top
        if(top>0):
            self.min = min(self.min, self.stack[top-1])
            self.max = max(self.max, self.stack[top-1])        

    def getMin(self):
        # Write your code here.
        return self.min

    def getMax(self):
        # Write your code here.
        return self.max

stack1 = MinMaxStack()

print(stack1.push(5))
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
print(stack1.peek())



