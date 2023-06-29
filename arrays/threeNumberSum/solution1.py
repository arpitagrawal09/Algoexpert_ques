def threeNumberSum(array, targetSum):
    # Write your code here.
    array.sort()
    triplets = []
    for i in range(len(array)):
        num1 = array[i]
        for j in range(i+1, len(array)):
            num2 = array[j]
            for k in range(j+1, len(array)):
                num3 = array[k]
                if (num1 + num2 + num3 == targetSum):
                    triplet = [num1, num2, num3]
                    triplet.sort()
                    triplets.append(triplet)
    return triplets
