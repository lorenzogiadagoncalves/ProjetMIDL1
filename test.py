from datastructs import *
from fonctions import *

f1 = Var("a")
f2 = FF()
f3 = And(Var("a"),Var("b"))
f4 = Or(Var("a"),Var("b"))
f5 = Impl(Var("a"),Var("b"))
f6 = Or(Impl(And(Var("a"), FF()), Not(Var("b"))), Var("a"))
lf = [f1,f2,f3,f4,f5,f6]

def makeVars(*vars: list[str]):
    """
    fonction qui instancie une nombre x de variables propositionnelles
    """
    if len(vars) == 1:
        return (Var(vars[0]))
    return tuple([Var(var) for var in vars])

def runTest() -> None:
    ...

if __name__ == "__main__":
    runTest()