"""digit = int("6")
digit = digit + digit
print(digit)"""

"""corresponding = {
    "1" : ["a", "b"],
    "2" : ["c", "d"]
}
for number in corresponding:
    for letter in corresponding[number]:
        print(letter)"""

"""array = [0, 1, 2]
del array[1]
print(array)
"""
"""def cleanBrackets(brackets):
    reducedStr = ""
    literals = ["(", ")", "[", "]", "{", "}"]
    for literal in brackets:
        if literal in literals:
            reducedStr += literal
    brackets = reducedStr
    return brackets

brackets = "{}gawgw()"
print(cleanBrackets(brackets))"""

"""pairs = {"(":")", "[":"]"}
if pairs["("]==")": print("yes")"""


"""alphabetSeq = {"A":1, "B":2}
print(alphabetSeq)
print(alphabetSeq["A"])
if 1 in alphabetSeq:    print("yes")
for pair in alphabetSeq:
    if pair"""

"""def getI(i):
    l = 7
    i = i%l
    if i < 0 : i = i + l
    print(i)

getI(-18)"""

"""i = 0
b = 1
while(1):
    if(i>=3): break 
    i+=1
    print(i)"""

"""group = {2, 4, 5}
group.update({9})
print(group)

if 19 in group:
    print(-1)"""

"""array = [0, 1, 2, 3, 4]
iMid = 5//2
array1 = array[0:iMid-1]
print(array1)
"""
"""num = 529 
print(num//10)

def maxMul(num):
    num = maxMul(num//10)
    if num==0 : return count"""


"""i = 1
j = 1
while(i<=8):
    while(j<=2):
        if(i == 4):
            break
        j+=1 
    i+=1
    j=1

print(i)
    """


"""def twoNumberSum(array, targetSum):
    nums = {}
    tS = targetSum
    for num in nums:
        compNum = tS - num
        if compNum in nums:
            return [num, compNum]
        else: 
            nums[num] = 'num'
    return []

nums = [2,7,11,15]
target = 9
ans = [0, 1]

nums = [3,2,4]
target = 6

nums = [3,3]
target = 6"""