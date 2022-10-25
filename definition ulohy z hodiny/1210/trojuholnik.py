def faktorial(cislo):
    vysledok = 1
    for i in range(2, cislo+1):
        vysledok *= i
    return vysledok

# vypocet = faktorial(5)
# print(faktorial(60))

def kombcislo(n,k):
    return faktorial(n)//(faktorial(k)*faktorial(n-k))

# print(kombcislo(5,3))

def pasc(riadok:int):
    for cisloriadku in range(riadok+1):
        for k in range(0, cisloriadku+1):
            print(kombcislo(cisloriadku,k),end="")
        print('')

pasc(5)

