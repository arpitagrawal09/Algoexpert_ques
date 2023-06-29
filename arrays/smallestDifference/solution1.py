def smallestDifference(arrayOne, arrayTwo):
    # Write your code here.
    l1 = len(arrayOne)
    l2 = len(arrayTwo)
    minDist = 10000000000000000000
    closestInts = [0.5, 0.5]
    for i in range(l1):
        for j in range(l2):
            node1 = arrayOne[i]
            node2 = arrayTwo[j]
            diff = node1 - node2
            nowDist = abs(diff)
            if(nowDist<minDist):
                minDist = nowDist
                closestInts = [node1, node2]

    return closestInts
            