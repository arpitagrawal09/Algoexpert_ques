#Successful submission. Solution 1. At Algoexpert
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def middleNode(linkedList):
    pointedNode = linkedList  
    l = 0
    while pointedNode is not None:
        l+=1
        pointedNode = pointedNode.next 

    iMid = (l+2)//2
    i = 1
    pointedNode = linkedList 
    while(i<iMid):
        pointedNode = pointedNode.next
        i+=1
        
    # Write your code here.
    return pointedNode
