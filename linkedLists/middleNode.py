class LinkedList:
    def __init__(self, val):
        self.next = None
        self.val = val
        
    def getLength(self):
        l = 0
        pointedNode = self
        while pointedNode is not None:
            l+=1
            pointedNode = pointedNode.next 

        return l
    
    def getMiddleNode(self):
        l = self.getLength()
        iMiddle = (l + 2)//2 
        pointedNode = self
        i=1
        while(i<iMiddle):
            pointedNode = pointedNode.next
            i+=1

        middleNode = pointedNode
        return middleNode
        
linkedList = LinkedList(-1)

n2 = LinkedList(3)
linkedList.next = n2

n3 = LinkedList(39)
n2.next = n3

n4 = LinkedList(10)
n3.next = n4      

n5 = LinkedList(4)
n4.next = n5

middleNode = linkedList.getMiddleNode()
print(middleNode.val)