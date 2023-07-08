def squareRoot(num):
    lo = 1
    hi = num
    while(hi>=lo):
        mid = (hi + lo)//2
        square = mid * mid 
        if(square == num): return mid
        elif(square > num):
            lower = mid - 1
            lowerBound = lower * lower 
            if(lowerBound < num): return lower
            else:hi = mid - 1
        else:
            higher = mid + 1
            higherBound = higher * higher 
            if(higherBound > num): return higher 
            else: lo = mid + 1

print(squareRoot(21))        #4
print(squareRoot(1))        #1
print(squareRoot(251))      #16
print(squareRoot(256))      #16