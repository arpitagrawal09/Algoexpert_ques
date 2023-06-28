class LinkedList:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None
    
    def findIntLL(self):
        num = 0
        node = self
        pos = 1
        multiplier = 1
        while(node is not None):
            digit = node.value
            placeVal = digit * multiplier
            num+=placeVal
            pos+=1
            node = node.next
            multiplier *= 10
           
        return num
    
"""number1 = LinkedList(4)
digit2 = LinkedList(5)
number1.next = digit2
digit3 = LinkedList(6)
digit2.next = digit3
number = number1.findIntLL()
print(number)"""

"""number1 = LinkedList(0)
digit2 = LinkedList(1)
number1.next = digit2
digit3 = LinkedList(0)
digit2.next = digit3
number = number1.findIntLL()
print(number)"""

"""number1 = LinkedList(4)
digit2Num1 = LinkedList(7)
number1.next = digit2Num1
digit3Num1 = LinkedList(2)
digit2Num1.next = digit3Num1
digit4Num1 = LinkedList(6)
digit3Num1.next = digit4Num1
number = number1.findIntLL()
print(number)

number2 = LinkedList(8)
digit2Num2 = LinkedList(6)
number2.next = digit2Num2
digit3Num2 = LinkedList(9)
digit2Num2.next = digit3Num2
digit4Num2 = LinkedList(6)
digit3Num2.next = digit4Num2
number = number2.findIntLL()
print(number)"""

number1 = LinkedList(4)
#digit2Num1 = LinkedList(7)
#number1.next = digit2Num1
"""digit3Num1 = LinkedList(2)
digit2Num1.next = digit3Num1
digit4Num1 = LinkedList(6)
digit3Num1.next = digit4Num1
number = number1.findIntLL()
print(number)"""

number2 = LinkedList(8)
#digit2Num2 = LinkedList(6)
#number2.next = digit2Num2
"""digit3Num2 = LinkedList(9)
digit2Num2.next = digit3Num2
digit4Num2 = LinkedList(6)
digit3Num2.next = digit4Num2
number = number2.findIntLL()
print(number)"""


def sumInt(l1, l2):
    num1 = l1.findIntLL()
    num2 = l2.findIntLL()
    sum = num1 + num2
    #print(sum)
    sumLL = LinkedList(-1)
    node = sumLL
    nDigits = 0
    while(sum != 0):
        digit = sum % 10 
        node.value = digit
        #print(node.value)
        if(sum>9):
            nextNum = LinkedList(-1)
        else:
            nextNum = None
        node.next = nextNum
        node = node.next
        sum = sum//10
    
    #print(sumLL.findIntLL())
    return sumLL 

sumLL = sumInt(number1, number2)
print(sumLL.findIntLL())