def pektroj(cislo:int):
    for i in range(cislo):
        print(" " * (cislo-i) + "*" * (2*i+1))
pektroj(10)