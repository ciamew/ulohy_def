# Napíš funkciu riadok(n, text=''), ktorá vypíše n znakový reťazec hviezdičiek '*', stred ktorého nahradí zadaným textom.
# Ak je tento zadaný text neprázdny, vloží na jeho začiatok aj koniec medzeru.

def riadok(pocethviezd:int, text:str):
    zaciatok = int(pocethviezd/2)
    koniec = int(pocethviezd/2)
    print(zaciatok*"*" ,text, koniec*"*")
    if len(text) == 0:
        print(riadok(sir))
sir = 50
print(riadok(sir,"jan botto"))
print(riadok(sir, "zlta lalija"))
print(riadok(sir))

?