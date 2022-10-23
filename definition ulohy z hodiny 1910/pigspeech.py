def pigspeech(slovo:str)->str:
    #noveslovo=""
    if len(slovo)>3:
        noveslovo = slovo[1::] + slovo[:1:] #alebo [0]
        noveslovo += "ya"
    else:
        noveslovo = slovo
    return noveslovo
print(pigspeech("ahoj"))