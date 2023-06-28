def isPalindrome(str):
    isPal = False
    l = len(str)
    i = 0
    while(i<l):
        iRev = -(i+1)
        eFwd = str[i]
        eRev = str[iRev]
        if(eFwd == eRev):
            i+=1
        else:
            break

    if i == l:
        isPal = True
    return isPal

print(isPalindrome("aba"))
print(isPalindrome("abc"))