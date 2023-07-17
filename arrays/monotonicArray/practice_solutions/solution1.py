#This solution did not pass any test case at algoexpert as on 17/07
#Complexities not tried
#Official solution seen : possibly not  

def isMonotonic(array):
    # Write your code here.
    l = len(array)

    prevTrend = "neutral"
    idealTrend = "no guess as of now"
    if(array[0]>array[1]):
        prevTrend = "non-increasing"
    elif(array[0]<array[1]):
        prevTrend = "non-decreasing"
    else: 
        prevTrend = "neutral"

    i = 1
    nowTrend = "neutral"
    isMonotonic = False
    while(i<l-1):
        if(array[i]<array[i+1]):
            nowTrend = "non-decreasing"
        elif(array[i]>array[i+1]):
            nowTrend = "non-increasing"
        else:
            nowTrend = "neutral"

        if(i==l-2):
            if((nowTrend == prevTrend)|(nowTrend == "neutral")): 
                isMonotonic = True
                break
            else:
                isMonotonic = False 
                
        if ((prevTrend == nowTrend) | (nowTrend == "neutral")):
            i+=1
            prevTrend = nowTrend
        else : break

    return isMonotonic 
        
