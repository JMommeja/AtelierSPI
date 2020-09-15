def Calcule1 (L:list):
    """Calcule de somme sur liste"""
    somme = 0
    i=0
    for i in range(len(L)) :
        somme+=L[i]
    return somme
    for e in L :
        somme+=e
    return somme
    while i < len(L) :
        somme+=L[i]
    return somme

#ma_list = [1,5,9]
#print (Calcule1(ma_list))

def test_exercice1():
    print("testsomme")
    #test liste vide
    print("test liste vide : ", Calcule1([]))
    #test somme 11111
    S=[1,10,100,1000,10000]
    print("test somme 11111 : ", Calcule1(S))
  
          
test_exercice1() 

def Moyenne (L:list):
    """Calcule de la moyenne sur liste"""
    somme = 0
    i=0
    for i in range(len(L)) :
        somme+=L[i]
    return somme/(i+1)
    for e in L :
        i+=1
        somme+=e
    return somme/(i+1)
    while i < len(L) :
        somme+=L[i]
    return somme/(i+1)

ma_list = [1,50,9]
print (Moyenne(ma_list))

def nb_sup(L,e):
    i=0
    
    for i in range(len(L)) :
       if L[i]>e:
        return L[i]
    for a in L :
        if L[a]>e:
         return L[a]

print (nb_sup(ma_list, 2))

def moy_sup(L,e):
    i=0
    somme = 0
    compt=0
    for i in range(len(L)) :
        if L[i]>e:
            compt+=1
            somme+=L[i]
    return somme/(compt)

print(moy_sup(ma_list, 6))

def ind_max(L):
    return len(L)-1

print(ind_max(ma_list))

def val_max(L):
   return max (L)

print(val_max(ma_list))

