class BST:
    def __init__(self, value) :
        self.left = None
        self.value = value
        self.right = None

def validatebst(tree, max = 1000, min = -1000):
    if tree is None :   return False
    
    v = tree.value
    left = tree.left
    right = tree.right
    isValidL = False
    isValidR = False

    if left is not None:
        if(left.value >= v): 
            return False    
        else:
            vL = left.value
            if(vL >= max): isValidL = False
            else:                
                isValidL = validatebst(left, v, min)
    else: isValidL = True
    if isValidL == False: return False


    if right is not None:
        vR = right.value
        if(vR < v): 
            return False    
        else:
            if(vR < min): isValidR = False
            else:
                isValidR = validatebst(right, max, v)
    else: isValidR = True
    if isValidR == False: return False

    if((isValidL==True)&(isValidR==True)):
        return True


bst00=None
#print(validatebst(bst00))

bst1B=BST(53)
n4 = BST(4)
bst1B.right = n4
#print(validatebst(bst1B, -10, 10))


bst1A=BST(53)
n4 = BST(4)
bst1A.left = n4
#print(validatebst(bst1A))


bst2A=BST(53)

n31 = BST(31)
bst2A.left = n31
n81 = BST(81)
bst2A.right = n81
#print(validatebst(bst2A))


bst2B=BST(53)

n31 = BST(31)
bst2B.right = n31
n81 = BST(81)
bst2B.left = n81

"""n51 = BST(51)     
n31.right = n51
n28 = BST(28)
n31.left = n28"""
#print(validatebst(bst2B))


bst3=BST(53)

n31 = BST(31)
bst3.left = n31
n81 = BST(81)
bst3.right = n81

n51 = BST(51)     
n31.right = n51
n28 = BST(28)
n31.left = n28

#print(validatebst(bst3))


bst4=BST(53)

n31 = BST(31)
bst4.left = n31
n81 = BST(81)
bst4.right = n81

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

#print(validatebst(bst4))


bst5=BST(53)

n31 = BST(31)
bst5.left = n31
n81 = BST(81)
bst5.right = n81

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

#print(validatebst(bst5))









