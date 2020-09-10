def annee_bissex (anne):
    res = ""
    if anne %4 == 0 :
        res = "bissex"
    else:
        res = "normal"
    return res

def fonction_test():
    print (annee_bissex (60))
    print (annee_bissex (10))
    print (annee_bissex (2019))
    print (annee_bissex (2020))

fonction_test()