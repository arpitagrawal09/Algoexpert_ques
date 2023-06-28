strA = "abcde"
k = 2
modified = ""
for i in range(0, k):
    modified += strA[i]
for i in range(k+1, len(strA)):
    modified += strA[i]
strA = modified
print(strA)



"""arr = [1, 2, 3]
del arr[0]
print(arr)"""


"""listFruits = ["apple", "mango", "strawberry"]
listFruits.remove("apple")
print(listFruits)
listFruits.insert(1, "apple")
print(listFruits)"""

"""charMatched = ["q", "s", "y", "s", "q"]
setAns = set(charMatched)
print(setAns)
listAns = []
for char in setAns:
    listAns.append(char)
print(listAns)"""

"""charMatched = [1, 2, 3, 2, 1]
setAns = set(charMatched)
print(setAns)
listAns = []
listAns.append(setAns)
print(listAns)"""

"""str1 = "meoutr"
str2 = "ideoit"

l1 = len(str1)
l2 = len(str2)

charMatched = {"-25322"}
for i in range(l1):
    if str1[i] in str2:
        charMatched.update({str1[i]})
print(charMatched)"""