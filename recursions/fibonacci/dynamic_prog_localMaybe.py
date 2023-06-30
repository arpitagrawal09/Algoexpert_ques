def getFibonacci(n):
    if n == 1: return 0
    if n == 2: return 1

    series = [0, 1]
    for i in range(2, n):
        series.append(series[i-1]+series[i-2])
    return series 

s1 = getFibonacci(1) 
s2 = getFibonacci(2)   
s3 = getFibonacci(3)
s4 = getFibonacci(6)

print(s4)