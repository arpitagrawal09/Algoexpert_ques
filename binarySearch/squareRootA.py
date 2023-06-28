def squareRoot(num):
	lo = 0
	hi = num
	while(hi >= lo):
		mid = (hi + lo)//2
		if(mid * mid == num):
			return mid
		if(mid * mid > num):
			hi = mid - 1
		else:
			lo = mid + 1
    return (lo - 1)

print(squareRoot(21))       #4
print(squareRoot(1))        #1
print(squareRoot(251))      #16
print(squareRoot(256))      #16