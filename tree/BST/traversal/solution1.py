def inOrderTraverse(tree, array):
    if tree is None: return None
    left = tree.left
    right = tree.right
    if left is not None:
        array = array + inOrderTraverse(left, [])
    array.append(tree.value)
    if right is not None:
        array = array + inOrderTraverse(right, [])
    return array 

def preOrderTraverse(tree, array):
    if tree is None: return None
    left = tree.left
    right = tree.right
    array.append(tree.value)
    if left is not None:
        array = array + preOrderTraverse(left, [])
    if right is not None:
        array = array + preOrderTraverse(right, [])
    return array 


def postOrderTraverse(tree, array):
    if tree is None: return None
    left = tree.left
    right = tree.right
    if left is not None:
        array = array + postOrderTraverse(left, [])
    if right is not None:
        array = array + postOrderTraverse(right, [])
    array.append(tree.value)    
    return array 

