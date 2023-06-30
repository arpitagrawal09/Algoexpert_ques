#Submission at Algoexpert. Solution 1. Accepted

# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def findLoop(head):
    # Write your code here.
    node = head 
    nodes = {None}
    while(node not in nodes):
        nodes.update({node})
        node = node.next
    return node
