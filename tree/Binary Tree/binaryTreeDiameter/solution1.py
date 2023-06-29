# This is an input class. Do not edit.
""" Program copied from my Algoexpert account on 6/29/23. The status is Yellow. Only 
1 solution is hosted in my account. 
"""
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def binaryTreeDiameter(tree):
    if tree is None : return -1
    diamInfo = getDiameter(tree)
    return diamInfo[1]-1

def getDiameter(tree):
    l = tree.left
    r = tree.right
    flag = None
    if ((l is None)&(r is None)):
        return [1, 1, "maxFromBranch"]
    if ((l is None)&(r is not None)):
        diamInfo = getDiameter(r)
        flag = "branch"
    if ((l is not None)&(r is None)):
        diamInfo = getDiameter(l)
        flag = "branch"
    if(flag == "branch"):
        if(diamInfo[2]=="maxFromTree"): 
            if(diamInfo[0]>=diamInfo[1]):
                diamInfo[1]=diamInfo[0]
                diamInfo[0]+=1
                diamInfo[1]+=1
                diamInfo[2]="maxFromBranch"
        else: 
            diamInfo[0]+=1
            diamInfo[1]+=1
        return diamInfo 
    diamInfoL = getDiameter(l)
    diamInfoR = getDiameter(r)
    lP = diamInfoL[0]
    rP = diamInfoR[0]   
    lM = diamInfoL[1]
    rM = diamInfoR[1]
    tP = lP + rP
    #if(lM>tP): maxD = lM - 1
    #if(rM>tP): maxD = rM - 1
    maxD = max(lM, rM, tP)
    p = max(lP, rP)
    return [p+1, maxD+1, "maxFromTree"]