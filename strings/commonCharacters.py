def commonChar(stringArr):
    l = len(stringArr)
    #charMatched = {"57r8392"}
    charMatched = []
    if(l > 0):
        strStart = stringArr[0]
        lStr = len(strStart)
    else:
        return charMatched
    for i in range(lStr):
        charMatched.append(strStart[i])

    for i in range(1, l):
        arr = stringArr[i]
        nCharsPrev = len(charMatched)
        j = 0
        while(j < len(charMatched)):
            char2Find = charMatched[j]
            if char2Find not in arr:
                charMatched.remove(char2Find)
            else: j += 1
            
        """for j in range(nCharsPrev):
            char2Find = charMatched[j]
            if char2Find not in arr:
                charMatched.remove(char2Find)"""
    
    return charMatched

stringArr = ["mqrpn", "qp", "qnrp"]
charMatched = commonChar(stringArr)
print(charMatched)

"""def commonChar(string):
    arrayLengths = []
    noOfStr = len(string)
    for i in range(noOfStr):
        arrayLengths.append(len(string[i]))
    smallestLen = -1
    for i in range(noOfStr):
        nowLen = len(string[i])
        if(nowLen < smallestLen):   smallestLen = nowLen
    
    for i in range(noOfStr):
        strReference = string[i]
        l = len(strReference)
        for j in range(i+1, l):
            strCheck = string[j]
            for k in range(l):
                charBase = strReference[k]
                char = ""

    charAll = []
    for i in range(noOfStr-1):
        str1 = string[i]
        str2 = string[i+1]"""
