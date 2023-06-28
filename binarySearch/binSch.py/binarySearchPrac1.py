def binarySearch(array, key):
    lo = 0
    hi = len(array-1)
    while(hi>lo):
        mid = (lo+hi)//2
        val = array[mid]
        if(val == mid): return mid
        elif(val < mid): hi = mid - 1
        else: lo = mid + 1
    return -1

