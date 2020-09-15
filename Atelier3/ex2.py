L= [1,2,4,5,0,15,65,55,959,795,4652]
def position (L,e):
     i=0
     for i in range(len(L)) :
       if L[i]==e:
           return i
print (position (L,5))
###def positionWhile (L,e):
###     i=0
###     while i <= (len(L)) :
###       if L[i]==e:
###           return i
###       else : 
###           i=+1
###print (positionWhile(L,5))
# MARCHE PAS ?????
def nb_occurence(L,e) :
     i=0
     Rep = ""
     while i < (len(L)) :
       if L[i]==e:
          Rep += str(i)+ ","
          i+=1
       else : 
           i+=1
     return Rep 
print (nb_occurence(L,5))

P= [1,6,7,8,9]
def est_triee(P):
    if P == sorted(P) :
        return " croissant"
    else : 
        return "pas croissant"

print (est_triee(P))

#def a_repetitions(L) :
#    T=[]



L= [1,-2,4,-5,0,15,65,55,959,0,795,-9999,4652,-5000]
def separer(L):
    LSEP=[]
    i=0
    DebutLSEP = 0
    FinLSEP=(len(L))
    for i in range(len(L)) :
        if L[i]<0:
            LSEP.insert(DebutLSEP, L[i])
            i+=1
            DebutLSEP+=1
        elif L[i]>0:
            LSEP.insert(FinLSEP, L[i])
            i+=1
            FinLSEP-=1
    for i in range(len(L)) :
        if L[i]==0:
            LSEP.insert(DebutLSEP , L[i])
            DebutLSEP+=1
      
          
    return LSEP 

print (separer(L))

def a_repetition(L):
    T = []
    i = 0
    Debut_liste=0
    while i < len(L):
        if L[i] in T:
            return "True"
        else:
            T.insert(Debut_liste,L[i])
            Debut_liste +=1
            i+=1
    return "False"

L = [1,2,3,4,5,6,2,3]
print(a_repetition(L))