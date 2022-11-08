#funkcia prejde retazcom a vrati priemer vsetkych cislic ktore tam najde

retazec = input("Zadaj retazec:")

def pisomka(retazec:str)->str:
    cislo = '1,2,3,4,5,6,7,8,9,0'
    sucet = 0
    pocet = 0
    for i in range(len(retazec)):
        if retazec[i] in cislo:
            sucet = sucet + int(retazec[i])
            pocet = pocet + 1
            priemer = sucet / pocet
            priemer = round(priemer,2)
        if priemer != 0:
            print("Priemer je:",priemer)
        else:
            print("")
        return ""
print(pisomka(retazec))
