# Naprogramuj funkciu, ktorá bude vypisovať (resp.vracať) n-ty znak v poradi v danom reťazci,
# ak samozrejme existuje. Pričom
# n - bude 1. parameter funkcie
# reťazec, v ktorom hľadáme bude 2.parameter funkcie
# Ak taký znak neexistuje, funkcia vypíšte vhodnú hlášku.

def uloha1(n, retazec:str)->str:
    if n >= len(retazec):
        print("zly index")
    else:
        print(retazec[n])
    return ""

print(uloha1(6,"kamikadze"))