def nonConstructibleChange(coins):
    # Write your code here.
    limitValue = 0
    coins.sort()
    for i in range(len(coins)):
        coin = coins[i]
        if (limitValue < (coin - 1)):
            break
        else: limitValue += coin
    minLimit = limitValue + 1
    return minLimit 

