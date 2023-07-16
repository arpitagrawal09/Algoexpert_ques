#Time complexity : suspense left for practice
#Arrange the queries in the order of lowest to highest. Keeping the lesser 
#time queries at front of the queue ensures that 
def minimumWaitingTime(queries):
    #Sorting gives the order of execution(left to right/ascending/non decreasing)
    queries.sort()
    #Initialisng the total waiting time as zero
    totalWaitingTime = 0
    #Initialising the waiting time of the oth query as zero
    lastWaitingTime = 0
    #Iterate and find out the waiting time for the full array
    for i in range(1, len(queries)):
        #waiting time for this query
        thisWaitingTime = lastWaitingTime + queries[i-1]
        #add this waiting time to total waiting time
        totalWaitingTime += thisWaitingTime
        #assign waiting time for the reference of the next query
        lastWaitingTime = thisWaitingTime
    #We have the minimum waiting time. return it 
    return totalWaitingTime 
