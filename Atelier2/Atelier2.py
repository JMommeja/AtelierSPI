def message_imc (imc):
    """" fonction qui permet de d'interpreter selon sont IMC (il a donc IMC en paramettre)"""
    statut = ""
    if imc < 16.5 :
        statut= "denutrition ou famine"
    elif imc < 18.5:
        statut= "maigreur"
    elif imc < 25:
        statut= "corpulence normale"
    elif imc < 30:
        statut= "surpoids"
    elif imc < 35:
        statut ="obésité modéré"
    elif imc < 40:
        statut= "obésité sévère"
    elif imc > 40:
        statut= "obésité morbide"
    return statut

def fonction_test():
    print (message_imc (60))
    print (message_imc (10))
    print (message_imc (20))
    print (message_imc (30))

fonction_test()