"""
This version has been fully accepted at Algoexpert. It passed all the test cases at once
This attempt should have taken <30 mins. I imagine to scale lesser than 15 mins at next
Complexities - left to practice
Keywords - key, search, sorted, integer, index

Another attempt at revising binary search. I am doing this after I got the question on search in a 2D array
Following the iterative method because I assume that its complexities are lesser 
"""

def binarySearch(array, target):
    # Write your code here.

    #initialise the range of search
    l = 0
    r = len(array)-1
    #break the loop when no element is found/indices start to breach into other
    while l!=r+1:
        #configure middle index
        mid = (l+r)//2
        #keep ready the middle integer
        numMid = array[mid]
        #search conditional statements
        #return the index in case of match
        if target==numMid:
            return mid
        #redefine the right boundary immediately left to the middle
        elif target < numMid:
            r = mid - 1
        #redefine the right boundary immediately right to the middle
        else:
            l = mid + 1
    #Entire array has been scanned without success. Flag a negative result 
    return -1
