def powerset(array):
    if len(array) == 0: return [[]]
    if len(array) == 1: return [[], array]
    thisSet = [[]]
    for i in range(len(array)):
        tempArr = array
        print(tempArr)
        print(i)
        del tempArr[i]
        thisSet += powerset(tempArr)
    thisSet += [array]
    uniqueSet = []
    [uniqueSet.append(val) for val in thisSet if val not in uniqueSet]
    return uniqueSet

set0 = []
set1 = [2]
set2 = [1, 3]
print(powerset(set2))