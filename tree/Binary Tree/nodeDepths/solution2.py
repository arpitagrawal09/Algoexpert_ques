def nodeDepths(root, depth=0):
    if root is None: return 0
    else :
        left = root.left
        right = root.right
        sumDepths = depth
        if left is not None:
            sumDepths += nodeDepths(root.left, depth + 1)
        if right is not None:
            sumDepths += nodeDepths(root.right , depth + 1)
        return sumDepths
    


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
