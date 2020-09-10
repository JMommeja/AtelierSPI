def descriminant ( a:float,b:float,c:float)-> float:
    """ calcul delta """
    return  b**2-4*a*c
   

def racine_unique(a:float,b:float) -> float:
    """calcul racine unique """
    return  -b/2*a
    
def racine_double(a:float,b:float,delta:float,num:float)->float:
    """renvoie la valeur  de la racine"""
    if num == 1:
        return  -b + delta**(0.5)/2*a
    else:
        return -b - delta**(0.5)/2*a

def str_equation(a,b,c)->str:
    """renvoie chaine caractere equation"""
    VALEUR_EGAL = 0
    equation = ""
    
    if(a!=0):
       if a == 1 :
           a = ""
       elif a==-1:
           a = "-"
       
       equation += str(a)+"x2 "     

    if(b!=0):
       if b == 1 :
           b = ""
       elif b==-1:
           b = "-" 
       if b>0 and a!=0 :
           equation+="+"
       equation += str(b)+"x"   
       
    if(c!=0):
      if c>0 and b!=0 :
           equation += "+"
      equation += str(c)
      
    equation+="=" + str(VALEUR_EGAL)
      
    return equation

def solution_equation(a:float, b:float, c:float):
    """renvoie chaine caractere redige"""

    if descriminant(a,b,c)<0:
        return "Solution equation "+str_equation(a,b,c)+" Pas de racine"
    if descriminant(a,b,c)==0:
        return "Solution equation ",a,"x2 + ",b,"x + ",c," = 0 une racine unique x="+racine_unique(a,b)
    if descriminant(a,b,c)>0:
        return "Solution equation ",a,"x2 + ",b,"x + ",c," = 0 deux racines""x1 =" 

    


print (str_equation(6.0,6.0,6.0))