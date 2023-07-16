#Solution one and two seem to be the same solutions written in a slightly different coding styles 
def minimumWaitingTime(queries):
    # Write your code here.
    queries.sort()
    minWaitingTime = 0
    prevWaitingTime = 0
    prevQueryTime = 0
    for i in range(len(queries)):
        thisWaitingTime = prevWaitingTime + prevQueryTime
        minWaitingTime += thisWaitingTime
        prevWaitingTime = thisWaitingTime
        prevQueryTime = queries[i]
    return minWaitingTime
