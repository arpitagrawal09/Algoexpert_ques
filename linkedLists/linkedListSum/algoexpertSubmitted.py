#Solution 1 submitted at Algoexpert. Accepted

# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def sumOfLinkedLists(linkedListOne, linkedListTwo):
    # Write your code here.
    num1 = 0
    node = linkedListOne
    pos = 1
    multiplier = 1
    while(node is not None):
        digit = node.value
        placeVal = digit * multiplier
        num1+=placeVal
        pos+=1
        node = node.next
        multiplier *= 10

    num2 = 0
    node = linkedListTwo
    pos = 1
    multiplier = 1
    while(node is not None):
        digit = node.value
        placeVal = digit * multiplier
        num2+=placeVal
        pos+=1
        node = node.next
        multiplier *= 10

    sum = num1 + num2
    if(sum==0):
        return LinkedList(0) 
    sumLL = LinkedList(-1)
    node = sumLL
    nDigits = 0
    while(sum != 0):
        digit = sum % 10 
        node.value = digit
        if(sum>9):
            nextNum = LinkedList(-1)
        else:
            nextNum = None
        node.next = nextNum
        node = node.next
        sum = sum//10

    return sumLL

    
