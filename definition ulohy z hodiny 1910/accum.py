def accum(slovo:int)->int:
    noveslovo = ""
    for i in range(len(slovo)):
        temp = slovo[i]*(i+1)
        temp = temp.capitalize()
        temp += "-"
        noveslovo += temp
    return noveslovo[:-1:] #odobera posledne -
print(accum("Tomas"))