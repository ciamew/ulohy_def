# Napíš funkciu obdlznik(sirka, znak='*'), ktorá z daného znaku znak vypíše do
# troch riadkov výstupu obdĺžnik zadanej šírky.

def obdlznik(cislo:int, znak:str):
    for i in range(1):
        print(cislo * znak)
        print(znak, ((cislo-4)*(" ")), znak)
        print(cislo * znak)
obdlznik(10,"#")
