def isDocFeasible(chs, d):
    lC = len(chs)
    lD = len(d)
    i = 0

    while((i>=0)&(i<lD)&(lC>0)&(lD>0)):
        if(d[i]==chs[lC-1]):
            #del chs[lC-1]
            #del d[i]
            strD = ""
            for j in range(0, i):
                strD += d[j]
            for j in range(i+1, lD):
                strD += d[j]
            d = strD
            strC = ""
            for j in range(0, lC - 1):
                strC += chs[j]
            chs = strC
            lC -= 1
            lD -= 1
        else:   i+=1
    if(lD==0):  return True
    else:   return False

chs1 = "myfggfm"
doc1 = "mfggy"
print(isDocFeasible(chs1, doc1))