def twoNumberSum(array, target):
    hT = {}
    for num in array:
        complement = target - num
        if complement in hT:
            return [num, complement]
        else:
            hT.add(num:True)
    return []


