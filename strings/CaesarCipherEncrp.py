def encrypted(str, k):
    str = 'a'
    str = int(str)
    return str

str = 'amy'
k = 55

"""while((new_val>=97) & (new_val<=122)):
    exceeds = new_val - 122 
    new_val = """

l = len(str)
strNew = ""
for i in range(l):
    char = str[i]
    ascii_val = ord(char)
    new_val = ascii_val + k
    while(new_val>122):
        exceeds = new_val - 122 
        new_val = 96 + exceeds
    charShifted = chr(new_val)
    #str[i] = charShifted
    strNew = strNew + charShifted
print(strNew)