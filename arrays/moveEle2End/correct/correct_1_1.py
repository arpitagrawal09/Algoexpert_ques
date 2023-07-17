#Accepted at algoexpert. No complexities calculations tried. No track(As on 17/07)

def moveElementToEnd(array, toMove):
    i = 0
    while(i<=len(array)-1):
        if(array[i])!=toMove:
            array.insert(0, array[i])
            del array[i+1]
        i+=1
    return array 