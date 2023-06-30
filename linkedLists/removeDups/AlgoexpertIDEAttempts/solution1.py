#Submitted solution 1 at Algoexpert. Accepted
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeDuplicatesFromLinkedList(linkedList):
    nodePointed = linkedList
    nodeNext = nodePointed.next 
    while(nodeNext!=None):
        #nodeNext = nodePointed.next 
        nowVal = nodePointed.value
        nextVal = nodeNext.value
        if(nowVal==nextVal):
            nodePointed.next = nodeNext.next
        else:
            nodePointed = nodeNext
        nodeNext = nodePointed.next
    return linkedList
