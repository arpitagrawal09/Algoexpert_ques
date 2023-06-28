class Queue:
    def __init__(self):
        self.elements = []
        self.rear = -1
        self.front = -1

    def dequeue(self):
        if self.front == -1: return -1
        del self.elements[self.front]
        self.front-=1

    def enqueue(self, element):
        l = len(self.elements)
        if self.front>=0:
            self.elements.append(0.5)
            for i in range(l):
                j = (l - 1) - i
                self.elements[j+1] = self.elements[j]
            self.elements[0] = element
        else: self.elements.append(element)
        self.front+=1

    def printQueue(self):
        qString = ""
        for i in range(len(self.elements)):
            qString += str(self.elements[i])
        print(self.elements) 

queue1 = Queue()
queue1.enqueue(1)
queue1.printQueue()
queue1.dequeue()
queue1.printQueue()
queue1.enqueue(7)
queue1.printQueue()
queue1.enqueue(-3)
queue1.printQueue()