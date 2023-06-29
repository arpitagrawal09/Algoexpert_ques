def findClosestValueInBst(tree, target):
    # Write your code here.
    val = tree.value
    diffnNow = target - val
    if(diffnNow == 0):
        return val
    else:
        if(diffnNow<0):
            next = tree.left
        else:
            next = tree.right
        if(next is not None):
            valNext = next.value
            diffnNext = target - valNext
            if(abs(diffnNext)<abs(diffnNow)):
                return findClosestValueInBst(next, target)
            else:
                return val 
        else:   
            return val


# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
