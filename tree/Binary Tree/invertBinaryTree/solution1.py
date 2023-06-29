def invertBinaryTree(tree):
    l = tree.left
    r = tree.right
    tree.left = r
    tree.right = l
    
    if(tree.right is not None):
        invertBinaryTree(tree.right)
    if(tree.left is not None):
        invertBinaryTree(tree.left)

# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
