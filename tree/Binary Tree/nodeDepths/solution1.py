def nodeDepths(root):
    if root is None : return 0
    else:
        depthsSum = 1
        if(root.left is not None): depthsSum += 2 * nodeDepths(root.left)
        if(root.right is not None): depthsSum += 2 * nodeDepths(root.right)        
        return depthsSum

# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
