# This is an input class. Do not edit.
class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

    def printNL(self):
        node = self
        doubleArrow = "<-->"
        nLStr = str(node.value)
        node = self.next
        while(node is not None):
            element = node.value
            thisStr = doubleArrow + str(element)
            nLStr += thisStr
            node = node.next
        print(nLStr)

# Feel free to add new properties and methods to the class.
class DoublyLinkedList :
    def __init__(self):
        self.head = None
        self.tail = None

    def setHead(self, node):
        # Write your code here.
        self.head = node 
        self.head.prev = None

    def setTail(self, node):
        # Write your code here.
        self.tail = node
        self.tail.next = None

    def insertBefore(self, node, nodeToInsert):
        # Write your code here.
        nodeToInsert.prev = node.prev
        node.prev.next = nodeToInsert 

        node.prev = nodeToInsert
        nodeToInsert.next = node 

    def insertAfter(self, node, nodeToInsert):
        # Write your code here.
        nodeToInsert.next = node.next
        node.next.prev = nodeToInsert
        node.next = nodeToInsert
        nodeToInsert.prev = node

    def insertAtPosition(self, position, nodeToInsert):
        # Write your code here.
        
        if(position == 1):
            nodeToInsert.next = self.head
            self.head.prev = nodeToInsert
            self.head = nodeToInsert
            nodeToInsert.prev = None
        else:
            l = 0
            node = self.head
            while node is not None:
                l += 1
                node = node.next
            if(position == l):
                self.tail.next = nodeToInsert
                nodeToInsert.prev = self.tail
                nodeToInsert.next = None
                self.tail = nodeToInsert 
                #nodeLeft = self.head
            else: 
                i = 1 
                while(i < position):
                    nodeLeft = nodeLeft.next
                    nodeRight = nodeLeft.next
                nodeMiddle = nodeToInsert
                nodeMiddle.next = nodeRight 
                nodeRight.prev = nodeMiddle
                nodeLeft.next = nodeMiddle
                nodeMiddle.prev = nodeLeft

    def removeNodesWithValue(self, value):
        # Write your code here.
        node = self.head
        while node is not None:
            if(node.value == value):
                nodeNext = node.next
                nodePrev = node.prev
                nodePrev.next = nodeNext
                nodeNext.prev = nodePrev
                node = nodeNext
            else:
                node = node.next

    def remove(self, node):
        # Write your code here.
        if node == self.head:
            self.head = self.head.next
            self.head.prev = None
            
        if node == self.tail:
            self.tail = self.tail.prev
            self.tail.next = None

        node.next.prev = node.prev
        node.prev.next = node.next 
    
    def containsNodeWithValue(self, value):
        # Write your code here.
        node = self.head
        nodes = []
        while node is not None:
            if node.value==value :
                return True 
            
    def printDLL(self):
        node = self.head
        arrow = "<-->"
        lLStr = ""
        while(node is not None):
            element = node.value
            nodeStr = arrow + str(element) 
            lLStr = lLStr + nodeStr
            node = node.next
        print(lLStr)

n14 = Node(4)
n231 = Node(5)
n231.prev = n14
n14.next = n231
n37 = Node(6)
n37.prev = n231
n231.next = n37
n31 = Node(31)
n37.next = n31
n31.prev = n37

n38 = Node(38)
n78 = Node(78)
n78.prev = n38
n38.next = n78
n7 = Node(8)
n7.prev = n78
n78.next = n7
n82 = Node(82)
n82.prev = n7
n7.next = n82
n5 = Node(5)
n82.next = n5
n5.prev = n82
n7 = Node(7)
n7.prev = n5
n5.next = n7  

n63 = Node(7)
n78 = Node(7)
n34 = Node(8)
n13 = Node(78)

dLL1 = DoublyLinkedList()
#n17.printNL()
dLL1.setHead(n38)
dLL1.printDLL()
dLL1.setHead(n82)



