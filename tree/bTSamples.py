class BT:
    def __init__(self, value):
        self.value = value 
        self.left = None
        self.right = None


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
