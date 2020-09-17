"""
------------------------------------
Author: Jean-eric Mommeja, Alexandre Motbal
Licence: libre
Name: Atelier 3 L3 spi
Date: 15/09/2020
------------------------------------
"""

import re
import os
#Exercice 1 partie 1
def full_name(str_arg:str)->str:
    """On utilise les fonctions pythons de manipulation de caractère,
    La fonction demande une string au format nom prénom,
    il sépare les deux mots en tableaux avec split(),
    puis on manipule le text"""
    tableau = str_arg.split(' ')
    tableau[0] = tableau[0].upper()
    tableau[1] = tableau[1].capitalize()
    result = tableau[0]+' '+tableau[1]

    return result


#exercice 1 partie 2
def is_mail(str_arg:str)->tuple:
    """La fonction is mail vérifie si l'entrée str_arg est valide il renverra que c'est ok
    le mail ne doit avoir qu'un arrobase, un seul point dans le nom de domaine, le nom de domaine ne peut finir par un caractère spécial"""
    if str_arg.find('@') == str_arg.rfind('@') and str_arg.find('@')>=0:
        tableau = str_arg.split('@')
        print(tableau)
        if tableau[1].find('.') == tableau[1].rfind('.') and tableau[1].find('.')>=0:
            nomDomaine = tableau[1].split('.')
            if nomDomaine[0][-1].isalnum():
                print('tout est ok')
            else:
                print('Le nom de domaine est incorrect')

        else:
            print('Le point n\'est pas bon')

    elif str_arg.find("@") == 0:
        print('Il n\'y a pas de corps')
    else:
        print('')

#is_mail('ouioui@univ-corse.fr')

#Exo 2 partie 1

def mots_Nlettres(lst_mot:list,n:str)->list:
    """La fonction prends une liste de mots et renvoie les mots comprenant le même nombre de lettre
    Il compare la longueur de chaque mots"""
    MotTrv = []
    for i in range(len(lst_mot)) :
        if len(lst_mot[i]) == n :
            MotTrv.append(lst_mot[i])
            i=+1
    return MotTrv

lst_mot = ["a","b","c","az","df","df"]

#print(mots_Nlettres(lst_mot,3))

def commence_par(mot:str,prefixe:str)->bool:
    """Dit si les mots ont le même préfixe, pour ce faire il regarde l'index des deux préfixes et les compares"""
    if mot.find(prefixe) == 0:
        return True
    else:
        return False

#print(commence_par("durandon","don"))

#exo3
def fini_par(mot:str,suffixe:str)->bool:
    """Dit si les mots ont le même suffixe, pour ce faire il regarde l'index des deux suffixes et les compares"""
    trv = False
    if mot.find(suffixe)>=0: 
        trv = True
    else : 
        trv = False
    return trv

#print(fini_par ("moooot","ot"))

#exo4
def finissent_par(lst_mot:list,suffixe:str)->list:
    res = []
    for n in lst_mot:
        if fini_par(n,suffixe) == True:
            res.append(n)
    return res
#print('Les mots sooooont :', end='')
#print(finissent_par(['cacahuette','alouette','pichette','buvette','grenouille','couteau','groseille'],'ette'))

def commencent_par(lst_mot:list,prefixe:str):
    res = []
    for n in lst_mot:
        if commence_par(n,prefixe) == True:
            res.append(n)
    return res
#print('Les mots sooooont :', end='')
#print(commencent_par(['cacahuette','alouette','pichette','buvette','grenouille','couteau','groseille'],'c'))

def liste_mots(lst_mot,prefixe,suffixe,n):
    step1 = commencent_par(lst_mot,prefixe)
    step2 = finissent_par(step1,suffixe)
    res = mots_Nlettres(step2,n)


    return res
#liste_mots(['cacahuette','culu','colu','calu','celu','alouette','pichette','buvette','grenouille','couteau','groseille'],'c','u',4)

def dictionnaire(fichier:str):
    f = open(fichier,"r")
    c = f.readline()
    
    print("DICTIONNAIRE")
    while c != "":
        print(c)
        c=f.readline()
    print("*FIN*")

dictionnaire(".\\mommeja\\AtelierSPI\\Atelier4\\littre.txt")