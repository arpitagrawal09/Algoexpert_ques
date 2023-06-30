def squareRoot(num):
    lo = 0
    hi = num
    while(lo<=hi):
        mid = (hi+lo)//2
        if(mid * mid == num):   return mid
        elif(mid * mid < num):  lo = mid + 1
        else :  hi = mid - 1
    return lo - 1

print(squareRoot(1))        #1
print(squareRoot(21))       #4
print(squareRoot(24))        #1
print(squareRoot(251))      #16
print(squareRoot(256))      #16