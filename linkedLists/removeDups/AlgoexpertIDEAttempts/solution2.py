#Submission at algoexpert. Accepted. Solution2
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeDuplicatesFromLinkedList(linkedList):
    # Write your code here.
    prevNode = linkedList
    pointedNode = prevNode.next
    all = {prevNode.value}
    while(pointedNode is not None):
        element = pointedNode.value
        if(element not in all):
            all.update({element})
            pointedNode = pointedNode.next
            prevNode = prevNode.next
        else:
            pointedNode = pointedNode.next
            prevNode.next = pointedNode
    return linkedList 
