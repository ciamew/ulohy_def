def uloha1(ret:str)->str:
    polka = len(ret) // 2
    if len(ret)%2 == 1:
        polka += 1
#cez rezy
    # pp = ret[0:polka].upper()
    # dp = ret[polka::]
    # return pp + dp
# print(uloha1("Tomas"))


# bez rezov
    dp = ""
    pp = ""
    for i in range(0, polka):
        pp += ret[i].upper()
    for i in range(polka, len(ret)):
        dp += ret[i]
    return pp + dp
print(uloha1("Tomas"))
