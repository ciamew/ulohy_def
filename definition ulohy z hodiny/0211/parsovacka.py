#funkcia vyberie znaky ktore nie su zapisane v <>

tr = "jano<dasdas>coze<kjhd>more<haha>"
def parsovacka (retazec:str)->str:
    nr=""
    Status = True
    for i in range(len(retazec)):
        if retazec[i] == "<":
            Status = False
            nr += ""
        if Status is True:
            nr += retazec[i]
        if retazec[i] == ">":
            Status = True
    return nr
print(parsovacka(tr))