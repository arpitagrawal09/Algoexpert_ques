#Practice attempt 1?

def moveElementToEnd(array, toMove):
    # Write your code here.
    l = len(array)
    i = 0
    count = 0
    while(i<l-1):
        if(array[i]==toMove):
            count+=1
            if(i + count == l -1):
                break 
            for j in range(i, l-1):
                array[j]=array[j+1]
            array[l-1]=toMove 
            i = 0
        else:
            i+=1
        
    return array 