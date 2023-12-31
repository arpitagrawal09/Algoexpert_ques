def sortedSquaredArray(array):
    length = len(array)
    l = 0
    r = length - 1
    while(r!=l+1):
        eL = abs(array[l])
        eR = abs(array[r])
        if eL > eR: l+=1
        elif eR == eL: l+=1
        else: r-=1
    sorted = [0] * length
    i = 0
    while i<length:
        if l==-1: 
            break
        if r==length:
            break
        eL = array[l]
        eR = array[r]
        squareLeft = eL * eL
        squareRight = eR * eR
        if squareLeft == squareRight:
            sorted[i]=squareLeft
            l -=1         
        elif squareLeft < squareRight:
            sorted[i]=squareLeft
            l -=1
        else:
            sorted[i]=squareRight
            r +=1
        i+=1
    if l==-1 and r != length:
        while(r<length):
            sorted[i]=array[r]*array[r]
            r+=1
            i+=1
    elif r==length and l!=-1:
        while(l>-1):
            sorted[i]=array[l]*array[l]
            l-=1
            i+=1
    return sorted

array1 = [-7, 5, 9]
sorted = sortedSquaredArray(array1)
print(sorted)