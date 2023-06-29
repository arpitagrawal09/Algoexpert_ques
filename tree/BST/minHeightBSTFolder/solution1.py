def minHeightBst(array):
    if array == []: return None 
    mid = (len(array)-1)//2
    aLeft = array[0 : mid]
    aRight = array[mid+1 : ]    
    self = BST(array[mid])
    left = minHeightBst(aLeft)
    right = minHeightBst(aRight)
    self.left = left
    self.right = right 
    return self

class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)
