# Do not edit the class below except
# for the depthFirstSearch method.
# Feel free to add new properties
# and methods to the class.
class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def depthFirstSearch(self, array):
        if self is None: return []
        array.append(self.name)
        neighbours = self.children
        if neighbours == []: return array
        for neighbour in neighbours:
            array+=neighbour.depthFirstSearch([])
        return array 
