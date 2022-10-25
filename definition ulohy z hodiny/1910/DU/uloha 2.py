# Naprogramuj funkciu, ktora bude mat jeden parameter a to retazec.
# Funkcia bude vracať počet číslic v reťazci.

def uloha2(retazec):
    pocet = 0
    cislica = "1,2,3,4,5,6,7,8,9,0"
    for i in range(len(retazec)):
        if retazec[i] in cislica:
            pocet += 1
    return pocet

print(uloha2("Na farme mame od roku 2012 12 kráv a 230 oviec."))
