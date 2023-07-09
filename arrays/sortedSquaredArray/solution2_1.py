def sortedSquaredArray(array):
    l = len(array)
    i = -1
    for i in range(l):
        if array[i]<=0 and array[i+1]>=0:
            break
    left = i
    right = i+1
    finalArray = []
    while(left>=0) and (right<l):
        squareLeft = array[left]*array[left]
        squareRight = array[right]*array[right]
        if(squareLeft>=squareRight):
            finalArray.append(squareLeft)
            left -= 1
        else:
            finalArray.append(squareRight)
            right += 1                    
    if left>0:
        for i in range(left, 1):
            finalArray.append(array[left]*array[left])
    if right<l-1:
        for i in range(right, l):
            finalArray.append(array[right]*array[right])
    return finalArray