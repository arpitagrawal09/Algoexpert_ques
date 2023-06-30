#Submission at Algoexpert. Solution 1. Accepted
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeKthNodeFromEnd(head, k):
    # Write your code here.
    node = head
    l = 0
    while node is not None:
        l += 1
        node = node.next

    if(k==l):
        head.value = head.next.value
        head.next = head.next.next
    else:
        fwdPosition = l - k + 1
        nodeNow = head.next
        nodeBack = head
        i = 2    
        while i < fwdPosition:
            nodeNow = nodeNow.next
            nodeBack = nodeBack.next
            i += 1
            
        nodeBack.next = nodeNow.next
        



        
