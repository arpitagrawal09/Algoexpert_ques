def runLE(string):
    l = len(string)
    encStr = ""
    i = 0
    while(i<l):
        char = string[i]
        count = 0
        #print(count)
        isBoundaryTouched = False
        for j in range(i, l):
            nowChar = string[j]
            if(nowChar == char):
                count = count + 1
                if(j >= l - 1): isBoundaryTouched = True
            else:
                i = j
                break
        if(count==1):
            newEnc = char
            encStr += newEnc
        elif((count<9) & (count>0)):
            newEnc = str(count) + char
            encStr += newEnc
        else:
            rem = count % 9
            multiplierOf9 = count // 9 
            if(rem==0):
                encRemainder = ""
            else :  encRemainder = str(rem) + char
            encNine = str(9) + char
            encMultiplesNine = ""
            for k in range(multiplierOf9):
                encMultiplesNine += encNine
            newEnc = encMultiplesNine + encRemainder
            encStr += newEnc
        if(isBoundaryTouched==True):
            break
    return encStr  

str1 = "rrrb"
str2 = "rbc"
str3 = "43^^hiiiiiopppppppppppppppppppppppppppppppppppp"

testCase1 = "AAAAAAAAAAAAABBCCCCDD"
myCase1 = "AAAAAAAAAAAAB"
myCase2 = "BBBBBBBBBA"
print(runLE(myCase2))