# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent


def findSuccessor(tree, node):
    if node is None : return None
    if tree is None : return None 
    if node == tree : 
        return findSuccessor(node.right)
    left = node.left
    right = node.right 
    parent = node.parent
    if ((left is None) & (right is None)):
        if(parent.left==node): return parent
        while(parent.parent is not None):
            if(parent.parent.left == parent):
                break
        if(parent.parent is None): return None
        else: return parent.parent
    if((left is not None) & (right is None)):
        if(parent.right == node):
            return findSuccessor()
        else:return parent
    if((left is None) & (right is not None)):
        if(right.left is not None): return findSuccessor(right)
        return right
    if((left is not None) & (right is not None)):
        if(right.left is not None): return findSuccessor(right)
        return right 
