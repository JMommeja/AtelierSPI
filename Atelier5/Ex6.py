L= [1,-2,4,-5,0,15,65,55,959,0,795,-9999,4652,-5000,0]
def separer(L):
    LSEP=[]
    i=0
    DebutLSEP = 0
    FinLSEP=(len(L))
    Prev = 0
    for i in range(len(L)) :
        if L[i]<Prev:
            LSEP.insert(DebutLSEP, L[i])
            i+=1
            DebutLSEP+=1
        elif L[i]>Prev:
            LSEP.insert(FinLSEP, L[i])
            i+=1
            FinLSEP-=1
    for i in range(len(L)) :
        if L[i]==Prev[i]:
            LSEP.insert(DebutLSEP , L[i])
            DebutLSEP+=1
    return LSEP

print(separer(L))

def tri (L) :
    List_Tri = []
    Min_List= min(L)
    Max_List= max(L)
    Prev = 0
    DebutLSEP = 0
    FinLSEP=(len(L))
    for i in range(len(L)) :
        if L[i] == Min_List :
            List_Tr.insert(L[i])
            DebutLSEP+=1
            Prev = L[i]
        elif L[i]==Max_List : 
             List_Tr.append(L[i])




