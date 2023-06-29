def kadanesAlgorithm(array):
    sums = [array[0]]
    for i in range(1, len(array)):
        if(sums[i-1]>0):
            sums.append(array[i]+sums[i-1])
        else:sums.append(max(array[i], sums[i-1]+array[i]))
    ans = -47321937946894
    for i in range(0, len(sums)):
        ans = max(sums[i], ans)
    return ans 
