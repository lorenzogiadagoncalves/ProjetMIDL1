from datastructs import *

"""fonction qui instancie une nombre x de variables propositionnelles"""
def makeVars(*vars):
    if len(vars) == 1:
        return Var(vars[0])
    return tuple([Var(var) for var in vars])
