def minimizedStringLength(s) :
    l = len(s)
    i = (l-1)//2
    while((i>=0) & (i<l)):
        c = s[i]
        jL = i - 1
        jR = i + 1
        iShifted = -1
        l = len(s)
        while((jL>=0) & (jR<l)):
            newStr = ""
            cL = s[jL]
            cR = s[jR]
            if(cL == c):
                for k in range(l):
                    if k != jL:
                        newStr = newStr + s[k]
                iShifted = i - 1
                s = newStr 
                break
            elif(cR == c):
                for k in range(l):
                    if k != jR:
                        newStr = newStr + s[k] 
                s = newStr             
            else:
                jL -= 1
                jR += 1
        print(s)
        if(iShifted == i-1):
            i = i - 1
        else:
            i = i + 1
    return len(s)

str1 = "aaabc"
l1 = minimizedStringLength(str1)
print(l1)