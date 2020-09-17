def L_to_mot(mot,L):
    """"Retourne true ou false dependant si il y a la lettre choisi par l'utilisateur dans le mot""" 
    res = False
    if mot.find(L)>=0:
        res = True
    else : 
        res = False 
    return res

def placesLettres(char: str , mot : str ) -> list :
    #if L_to_mot(mot,char) == True :
    list_tri = []
    if L_to_mot(mot,char) == True :
        cpt = 0
        for l in mot:
            if l == char:
                list_tri.append(cpt)
            cpt +=1
    return list_tri

#print(placesLettres('a','maman'))

def outputStr(mot):
    taille = len(mot)
    for n in range(0,taille):
        if mot[n] == ' ':
            print(' ', end='')
        else:
            print('_',end='')
        
        print(' ',end='')
#outputStr('Zouglou, la danse des magiciens ! zouglou dance')
import random
def runGame():
    listeMot = ["Tartiflette","rutabaga","tobogan","redondindron","Hippopotame"]
    rng = random.randint(0,len(listeMot))
    outputStr(listeMot[rng])
    for i in range(0,5):
        lettre_guess = input("Lettre a entrer")
        if placesLettres(lettre_guess,listeMot[rng]):
            print('bien joué')
        else:
            print('Vous avez perdu une vie')
    print('perdu')
runGame()