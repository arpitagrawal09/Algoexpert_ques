class BST():
    def __init__(self, val) :
        self.val = val
        self.left = None
        self.right = None

    def lookup(self, key):
        node = self
        val = node.val
        if(val == key):
            return node
        elif(key<val):
            node = node.left
            return node.lookup(key) 
        else:
            node = node.right
            return node.lookup(key)
        
bst1 = BST(6)
n1L = BST(4)
n1R = BST(8)
bst1.left = n1L
bst1.right = n1R

key = 8
node = bst1.lookup(8)
print(node.val)