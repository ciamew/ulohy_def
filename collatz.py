# def collatz(cislo:int):
#     while cislo != 1:
#         if cislo % 2 == 0:
#             cislo = cislo // 2
#             print("Cislo po deleni 2 je:", cislo, end = " ")
#             print('')
#         else:
#             cislo = (cislo*3)+1
#             print("Cislo po nasobeni 3 a pripocitani 1 je:",cislo , end = " ")
#             print('')
# collatz(13)

def pek_troj(n:int):
    for i in range(n):
        print(" " * (n-i-1) + "*" * (2*i+1))

n = int(input("Zadaj n: "))
print(pek_troj(n))
