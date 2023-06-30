#Submission at Algoexpert. Solution 1. Accepted

# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def reverseLinkedList(head):
    # Write your code here.
    prevNode = head
    pointedNode = prevNode.next
    while(pointedNode is not None):
        prevNode.next = pointedNode.next
        pointedNode.next = head
        head = pointedNode 
        pointedNode = prevNode.next
    return head
