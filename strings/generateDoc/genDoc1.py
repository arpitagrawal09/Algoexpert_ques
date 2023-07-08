def isDocFeasible(chs, d):
    lC = len(chs)
    lD = len(d)
    i = 0

    while((i>=0)&(i<len(d))):
        charD = d[i] 
        j = 0
        found = False
        while((j>=0)&(j<len(chs))):
            if(charD==chs[j]):
                #del chs[lC-1]
                #del d[i]
                strD = ""
                for k in range(0, i):
                    strD += d[k]
                for k in range(i+1, len(d)):
                    strD += d[k]
                d = strD
                strC = ""
                for k in range(0, j):
                    strC += chs[k]
                for k in range(j+1, len(chs)):
                    strC += chs[k]                    
                chs = strC
                found = True
                break
            else : j += 1
        if(found == False): break
    if(len(d)==0):  return True
    else:   return False

chs1 = "dededg"
doc1 = "deddeg"
print(isDocFeasible(chs1, doc1))