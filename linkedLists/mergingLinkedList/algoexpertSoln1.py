# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def mergingLinkedLists(linkedListOne, linkedListTwo):
    # Write your code here.
    node1 = linkedListOne
    node2 = linkedListTwo
    while(node1 != None):
        while(node2 != None):
            if(node1==node2):
                break
            else:
                node2 = node2.next
        if(node1 == node2):
            break
        node1 = node1.next 
        node2 = linkedListTwo 
    node = None
    if(node1 != None):
        node = node1
    else:
        node = None
    return node
