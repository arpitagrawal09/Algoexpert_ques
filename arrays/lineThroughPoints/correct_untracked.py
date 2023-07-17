#Seems to be a correct attempt. But this solution might not have been tracked

def lineThroughPoints(points):
    # Write your code here.
    n = len(points)
    maxPointsPrev = 2
    maxPointsNow = 2
    
    for i in range(n-2):
        x1 = points[i][0]
        y1 = points[i][1]
        for j in range(i+1, n-1):
            #basis points and slope

            x2 = points[j][0]
            y2 = points[j][1]
            if(x2 == x1):
                for k in range(j+1, n):
                    x3 = points[k][0]
                    if(x3 == x2):
                        maxPointsNow+=1
            elif(y2 == y1):
                for k in range(j+1, n):
                    y3 = points[k][1]
                    if(y3 == y2):
                        maxPointsNow+=1
            #to find if the current point lies on the line 
            else:
                m = (y2 - y1)/(x2 - x1)
                for k in range(j+1, n): 
                    x3 = points[k][0]
                    y3 = points[k][1]
                    h = y3 - y1
                    b = x3 - x1
                    if(h == b*m): 
                        maxPointsNow+=1
            
            if(maxPointsNow>maxPointsPrev):
                maxPointsPrev = maxPointsNow
            maxPointsNow = 2
    if(n==1):
        maxPointsPrev = 1
    return maxPointsPrev 

