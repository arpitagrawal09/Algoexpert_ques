"""class LinkedList():
    def __init__(self, head) :
        self.head = None"""

class LinkedList():
    def __init__(self, value) :
        self.next = None
        self.value = value

def removeDuplicatesFromLinkedList(linkedList):
    # Write your code here.
    nodePointed = linkedList
    nodeNext = nodePointed.next 
    while(nodeNext.next!=None):
        #nodeNext = nodePointed.next 
        nowVal = nodePointed.value
        nextVal = nodeNext.value
        if(nowVal==nextVal):
            nodePointed.next = nodeNext.next
        else:
            nodePointed = nodeNext
        nodeNext = nodePointed.next
    return linkedList


linkedList = LinkedList(-1)
n1 = LinkedList(3)
linkedList.next = n1

n2 = LinkedList(5)
n1.next = n2

n3 = LinkedList(5)
n2.next = n3      

n4 = LinkedList(4)
n3.next = n4

"""def removeDuplicatesFromLinkedList(linkedList):
    node = linkedList.next
    while(node!=None):
        val = node.value
        next = node.next
        valNext = next.value 
        if(valNext==val):
            last = next.next
            node.next = last
            #node = node.next

    return None

def removeDuplicatesFromLinkedListPrac(linkedList):
    nodePointed = linkedList.next
    while(nodePointed!=None):
        nodeNext = nodePointed.next 
        nowVal = nodePointed.value
        nextVal = nodeNext.value
        if(nowVal==nextVal):
            nodePointed.next = nodeNext.next
        else:
            nodePointed = nodeNext"""

      