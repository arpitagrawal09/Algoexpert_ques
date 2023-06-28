def getNthFibo(n):
    if(n==0): return 0
    elif(n==1): return 1
    else:
        sum = getNthFibo(n-1) + getNthFibo(n-2)
        return sum
    
print(getNthFibo(7))