# Sumbmission at Algoexpert. Solution 1. Rejected 
# This is an input class. Do not edit.
class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

# Feel free to add new properties and methods to the class.
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def setHead(self, node):
        # Write your code here.
        nodeLeft = node.prev
        nodeRight = node.next
        nodeLeft.next = nodeRight.prev
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
