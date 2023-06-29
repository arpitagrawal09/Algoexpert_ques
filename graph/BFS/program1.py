# Do not edit the class below except
# for the breadthFirstSearch method.
# Feel free to add new properties
# and methods to the class.
class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def breadthFirstSearch(self, array):
        obj = BFS(self)
        return obj.getBFS()

class BFS:
    def __init__(self, graph):
        self.node = graph
        self.front = 0
        self.rear = 0
        self.nodes = []
        self.BFS = []

    def enqueue(self, node):
        if node is not None:
            self.nodes.append(node)
            self.rear += 1

    def dequeue(self):
        node = self.nodes[0]
        self.BFS.append(node.name)
        print(self.BFS)
        children = node.children
        for i in range(0, len(self.nodes)-1):
            self.nodes[i] = self.nodes[i+1]
        del self.nodes[len(self.nodes)-1]
        #del self.nodes[0]
        self.rear -= 1
        return children 
            
    def getBFS(self):
        children = [self.node]
        while(1):
            for i in range(len(children)):
                self.enqueue(children[i])
            if(self.rear == 0): break 
            if self.rear != 0 :
                children = self.dequeue()

        return self.BFS
        


















