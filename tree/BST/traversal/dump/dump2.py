class BT:
    def __init__(self, value):
        self.value = value 
        self.left = None
        self.right = None
    
    def inOrderTraversal(self):
        if(self is None):
            print(self.value)
        else:
            if self.left is not None:          
                self.left.inOrderTraversal()
            print(self.value)
            if self.right is not None:            
                self.right.inOrderTraversal()
    
    def preOrderTraversal(self):
        if(self is None):
            print(self.value)
        else:
            print(self.value)
            if self.left is not None:          
                self.left.preOrderTraversal()
            if self.right is not None:            
                self.right.preOrderTraversal()

    def postOrderTraversal(self):
        if(self is None):
            print(self.value)
        else:
            if self.left is not None:          
                self.left.postOrderTraversal()
            if self.right is not None:            
                self.right.postOrderTraversal()
            print(self.value)

bT1=BT(33)

n73 = BT(73)
bT1.left = n73
n8 = BT(8)
bT1.right = n8

n60 = BT(60)     
n73.left = n60
n28 = BT(28)
n73.right = n28

n30 = BT(30)
n28.right = n30

n48 = BT(48)     
n8.left = n48
n52 = BT(52)
n8.right = n52

#bT1.inOrderTraversal()
#bT1.preOrderTraversal()
bT1.postOrderTraversal()