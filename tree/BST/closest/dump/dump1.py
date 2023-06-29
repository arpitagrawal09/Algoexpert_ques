def findClosestValueInBst(tree, target):
    # Write your code here.
    val = tree.value
    if(target==val):
        return tree.value
    else:
        if(target<val):
            next = tree.left
        else:
            next = tree.right
        if(next is not None):
            return findClosestValueInBst(next, target)
        else:   return val

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
            diffnNext = tree.next.value - target
            if(abs(diffnNext)<abs(diffnNow)):
                return findClosestValueInBst(next, target)
            else:
                return val 
        else : return val
