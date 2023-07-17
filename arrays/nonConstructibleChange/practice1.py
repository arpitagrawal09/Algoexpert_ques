#har har sikka bad jadi kadi tab tak 
#ek bhi na choote beech daam jab tak  

def minConstructibleChange(coinArray):
    minChange = 0
    for i in range(len(coinArray)):
        nowCoin = coinArray[i]
        if nowCoin <= minChange + 1 : 
            minChange = minChange + nowCoin
        else : break
    return minChange

# coinArray1 = [1, 2, 4, 8, 12]
# coinArray2 = [1, 1, 3, 6, 9, 16]
minChange = minConstructibleChange(coinArray-passFromCommented)
print(minChange)
