class LinkedList:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None

lL1 = LinkedList(1)
n2 = LinkedList(2)
n3 = LinkedList(3)
n4 = LinkedList(4)

lL1.next = n2
n2.next = n3
n3.next = n4

lL2 = LinkedList(-1)
m2 = LinkedList(-2)
m3 = n3
m4 = n4

lL2.next = m2
m2.next = m3
m3.next = m4


def mergingPoint(lL1, lL2):
    node1 = lL1
    node2 = lL2
    while(node1 is not None):
        node2 = lL2
        while(node2 is not None):
            if(node1 == node2):
                break
            else:
                node2 = node2.next
        if(node1 == node2):
            break
        node1 = node1.next
    return node1


#    while(node1 is not None) & node2 is not None:
#        node2 = lL2
#        if(node1 == node2):
#           break
#        node2 = node2.next
#        node1 = node1.next
    
    print(node1.value)
    print("loop run baby")

""" if(node1 is not None):
        return node1
    else:   return None
"""

print(mergingPoint(lL1, lL2).value)
