# Naprogramuj funkciu samohlaskovy(retazec), ktora bude mat jeden parameter a to retazec.
# Funkcia bude zistovať či je reťazec samohlaskovy. T.j. bude vracať True, ak je retazec vyskladany
# iba zo samych samohlasok alebo False ak retazecobsahuje čo i len jednu spoluhlasku.
# Predpokladajme, ze na vstupe budu len pismena malej abecedy.

def uloha3(retazec):
    samohlaska = "aeiyou"
    for i in range(len(retazec)):
        if retazec[i] in samohlaska:
            return True
        else:
            return False

print(uloha3("ahoj"))
