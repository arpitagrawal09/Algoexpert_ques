class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def validateBst(tree):
    valNow = tree.value
    isRTrue = False
    isLTrue = False
    left = tree.left
    right = tree.right
    if(left is None): isLTrue = True
    else :
        valLeft = left.value
        if(valLeft < valNow):
            isLTrue = validateBst(left)
            if(isLTrue==False): return False
        else: return False
    if(right is None): isRTrue = True
    else:
        valRight = right.value
        if(valRight >= valNow):
            isRTrue = validateBst(right)
            if(isRTrue==False): return False
        else: return False
    if((isLTrue == True)&(isRTrue == True)):
        return True 
    
bst1=BST(10)

n5A = BST(5)
bst1.left = n5A
n15 = BST(15)
bst1.right = n15

n5B = BST(5)     
n5A.right = n5B
n2 = BST(2)
n5A.left = n2

n1 = BST(1)
n2.left = n1

n11 = BST(11)     
n5B.right = n11
n22 = BST(22)
n15.right = n22

print(validateBst(bst1))