#Solution has been tried at VSCode. Test Case should only be the botton one. 
#Code is giving the correct output. Code writing sytle seems to be long. 

def twoNumberSum(arr, target):
    l = len(arr)
    if l <= 1 : return -1
    i = 0
    j = 0
    num1 = -1
    num2 = -1
    doesPairExist = False
    for i in range(l-1):
        if(doesPairExist==True): break
        for j in range(i+1, l):
            num1 = arr[i]
            num2 = arr[j]
            if(arr[i]+arr[j]==target):
                doesPairExist = True
                break
        if(doesPairExist==True): break
    if doesPairExist == False: return -1
    return [arr[i], arr[j]]

print(twoNumberSum([1, 2, 3], 4))
    