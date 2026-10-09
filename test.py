from datastructs import *

def makeVars(*vars ):
    """
    fonction qui instancie une nombre x de variables propositionnelles
    vars: strings
    """
    if len(vars) == 1:
        return (Var(vars[0]))
    return tuple([Var(var) for var in vars])

def runTest() -> None:
    ...

if __name__ == "__main__":
    runTest()