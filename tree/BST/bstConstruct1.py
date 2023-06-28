class BST:
    def __init__(self, value) :
        self.left = None
        self.value = value
        self.right = None
    
    def insertNode(self, value):
        target = value
        nowVal = self.value
        if(target < nowVal):
            next = self.left
            if(next is None):
                insNode = BST(target)
                self.left = insNode 
                return self
            else:
                return next.insertNode(value)
        else :
            next = self.right
            if(next is None):
                insNode = BST(target)
                self.right = insNode 
                return self
            else:
                return next.insertNode(value)   
            
    def remove(self, target):
        left = self.left
        right = self.right
        val = self.value
        removeNode = None
        isFound = False 
        if left.value == target:
            removeNode = left
            if removeNode.left is None & removeNode.right is None:
                self.left = None
                return None
            if removeNode.left is not None & removeNode.right is None:
                self.left = removeNode.left
                return self.left 
            if removeNode.left is None & removeNode.right is not None:
                self.left = removeNode.right
                return self.left
        elif right.value == target:
            removeNode = right
            if removeNode.left is None & removeNode.right is None:
                self.right = None
                return None
            if removeNode.left is not None & removeNode.right is None:
                self.right = removeNode.left
                return self.right
            if removeNode.left is None & removeNode.right is not None:
                self.left = removeNode.right
                return self.right
        #if(target==val):
        #    if left is None:
        #        if right is None
        elif(target<val):
            if(left is None):
                return -1        
            else:
                next = self.left
                return next.remove(target)
        elif(target>val):
            if(right is None):
                return -1
            else : 
                next = self.right
                return next.remove(target)  
        elif(target==val): return "root node"          


    def contains(self, value):
        if self is None : return False
        target = value
        value = self.value 
        isContained = False
        if(target<value):
            if(self.left is not None):
                return self.left.contains(value)
            else:
                return False
        elif(target==value):
            return True
        else:
            if(self.right is not None):
                return self.right.contains(value)
            else:
                return False 

bst1=BST(53)

n31 = BST(31)
bst1.left = n31
n81 = BST(81)
bst1.right = n81

n51 = BST(51)     
n31.right = n51
n28 = BST(28)
n31.left = n28

n30 = BST(30)
n28.right = n30

n48 = BST(48)     
n51.left = n48
n52 = BST(52)
n51.right = n52

"""target1 = 37 
parentNode = bst1.insertNode(target1)
pValue = parentNode.value
chValue = parentNode.left.value 
print("The parent node with the value " + str(pValue) +  " is pointing to the inserted node with the value " + str(chValue) )"""
# Ans is ----

"""target1 = 51
removedValue = bst1.remove(target1)
print("The node with the value " + str(removedValue) +  " has been removed")"""
#Ans is ----

print(bst1.contains(53))