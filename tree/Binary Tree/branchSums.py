class BT:
    def __init__(self, value):
        self.value = value 
        self.left = None
        self.right = None

def branchSums(root):
    if root is None : return -1
    val = root.value
    left = root.left
    right = root.right
    sums = []
    if(left is not None):
        sums += branchSums(left)
    if(right is not None):
        sums += branchSums(right)
    for i in range(len(sums)):
        sums[i] += val
    if left is None:
        if right is None:
            sums = [val]
    return sums

bT1=BT(33)

n73 = BT(73)
bT1.left = n73
n8 = BT(8)
bT1.right = n8

n60 = BT(60)     
n73.left = n60
n28 = BT(28)
n73.right = n28

n30 = BT(30)
n28.right = n30

n48 = BT(48)     
n8.left = n48
n52 = BT(52)
n8.right = n52

bT2=BT(33)

n73 = BT(73)
bT2.left = n73
n8 = BT(8)
bT2.right = n8


allSums = branchSums(bT1)
print(allSums)