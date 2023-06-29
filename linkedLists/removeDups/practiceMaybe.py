class LinkedList:
    def __init__(self, value) :
        self.value = value
        self.next = None

    def getLL(self):
        node = self
        lLprint = str(node.value)
        arrow = "-->"
        node = node.next
        while(node!=None):
            element = node.value
            valString = arrow + str(element)
            lLprint = lLprint + valString
            node = node.next
        return lLprint

def removeDuplicatesFromLinkedList(linkedList):
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
    #print(all)
    #lLprint = prevNode.getLL()
    #print(lLprint)
    #prevNode = linkedList
    #pointedNode = prevNode.next
    """while(pointedNode is not None):
        value = pointedNode.value
        if value in all:
            prevNode.next = pointedNode.next
            pointedNode = prevNode.next 
        else :
            pointedNode = pointedNode.next
            prevNode = prevNode.next""" 
    
    return linkedList

#Test Case 1
"""lL1 = LinkedList(5)
n2 = LinkedList(2)
n3 = LinkedList(1)
n4 = LinkedList(3)
n5 = LinkedList(2)
n6 = LinkedList(4)
lL1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n6
"""

#Test Case 2
lL1 = LinkedList(7)
n2 = LinkedList(2)
n3 = LinkedList(2)
lL1.next = n2
n2.next = n3 

#print(lL1.getLL())
#print(lL1.getLL())
lLCleaned = removeDuplicatesFromLinkedList(lL1)
print(lLCleaned.getLL())