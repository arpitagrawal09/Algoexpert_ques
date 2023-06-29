def minimumAreaRectangle(points):
    # Write your code here.
    n = len(points)
    nowA = 0
    prevA = 1011
    for i in range(n-3):
        x1 = points[i][0]
        y1 = points[i][1]
        p1 = points[i]
        for j in range(i+1, n-2):
            x2 = points[j][0]
            y2 = points[j][1]
            p2 = points[j]
            for k in range(n-1):
                x3 = points[k][0]
                y3 = points[k][1]
                p3 = points[k]
                for l in range(k+1, n):
                    x4 = points[l][0]
                    y4 = points[l][1]
                    p4 = points[l]
                    quad = [p1, p2, p3, p4]
                    for 
                    
                    if((x1==x4)&(y4==y3)&(y2==y1)&(x3==x2)):
                        nowA = (y4-y1)*(x2-x1)
                        nowA = abs(nowA)
                        if(nowA<prevA):
                            prevA = nowA
                            nowA = -1
    if(prevA == 1011):prevA = 0
    return prevA

