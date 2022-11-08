def code(zdroj:str,word:str)->str:
    nc = ""
    zc = 0
    code1 = word
    for i in range(len(zdroj)):
        while len(zdroj) != len(code1):
            code1 += word[zc]
            zc = zc+1
            if zc == (len(word)-1):
                zc= 0
        a = ord(zdroj[i])
        b = ord(code1[i])
        a = (((a-97)+b)%26)+97
        c = chr(a)
        nc += c
    return nc
print(code("ahojsvet","macka"))