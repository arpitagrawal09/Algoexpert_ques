# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def evaluateExpressionTree(tree):
    if tree is None : return -1
    val = tree.value 
    l = tree.left
    r = tree.right
    if l is None : return val
    lV = evaluateExpressionTree(l)
    rV = evaluateExpressionTree(r)
    operandKey = val
    ans = 0 
    if (operandKey == -1): return lV + rV
    if (operandKey == -2): return lV - rV    
    if (operandKey == -3): return int(lV / rV)    
    if (operandKey == -4): return lV * rV