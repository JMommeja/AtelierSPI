from datetime import date

def date_est_valide(jour,mois,annee) :
    res = ""
    if jour <= 31 and mois <= 12:
       res = "Valide"
    else:
        res = "Pas valide"
    return res

def saisie_date_naissance() : 
    jour = int(input("Jour de naissance "))
    mois = int(input("mois de naissance "))
    annee = int(input("annee de naissance "))
    if  date_est_valide(jour,mois,annee) == "Valide" :
       datenaiss = date(annee , mois , jour)
       return datenaiss
    else :
        "Veilliez rentrez une date valide"
    
def age(date_naissance) :
    ajd = date.today() 
    res = (ajd - date_naissance)
    return res / 365

print (age(saisie_date_naissance()))