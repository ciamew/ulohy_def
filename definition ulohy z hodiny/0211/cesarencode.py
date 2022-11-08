#zoberiem znak premenim na cislo, odpocit 97,pripocitamposun, potom vydelim % 26

def cesarencode(zdroj:str,posun:int)->str:
    nr = ""
    for i in range(len(zdroj)):
        a = ord(zdroj[i])
        a = (((a-97)+posun)%26)+97
        b = chr(a)
        nr += b
    return nr
print(cesarencode("miso", 3))