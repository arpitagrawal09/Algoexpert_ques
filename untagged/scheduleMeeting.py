def meetingsSchedule(tT1, tT2):

    tT1 = []
    tT1 = [[10.20, 11.00], [11.25, 12.05]]
    #tT1 = [["10:20, 11:05"], ["11:20, 12:05"]]
    tT2 = [[10.20, 11.15], [11.20, 11.40]]

    l1 = len(tT1)
    l2 = len(tT2)
    dailyBound1 = [10.0, 6.0]
    dailyBound2 = [10.0, 6.0]
    availableBlocks = []
    for i in range(l1):
        opens1 = tT1[i][0]
        endTime1 = tT1[i][1]
        startTime2 = tT2[i][0]    
        if(startTime1 <= startTime2):
            startTime = 
    