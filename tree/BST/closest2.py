class BST:
    def __init__(self, value) :
        self.value = value
        self.right = None
        self.left = None

def findClosestValueInBst(tree, target):
    # Write your code here.
    diffMin = 100000000000000
    value = 1000000000000
    while(tree is not None):
        val = tree.value
        diffNow = abs(target - val)
        if(diffNow<diffMin):    diffMin = diffNow
        if(diffMin == 0):
            return val
        else: 
            if(target < val):
                tree = tree.left
            else:
                tree = tree.right
    return 

        

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

bst2 = None
val = findClosestValueInBst(bst2, 26)
print(val)