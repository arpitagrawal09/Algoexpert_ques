#Practice attempt 2?

def moveElementToEnd(array, toMove):
    i = 0
    while(i<len(array)-1):
        if array[i]==toMove:
            array.append(toMove)
            del array[i]
        else: i+= 1
    return array 
