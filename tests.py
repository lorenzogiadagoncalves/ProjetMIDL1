from datastructs import *

from rules import *

"""fonction qui instancie un nombre n de variables propositionnelles
*vars : n """
def makeVars(*vars:tuple[str]) -> tuple[Var]:
    if len(vars) == 1:
        return Var(vars[0])
    return tuple([Var(var) for var in vars])


def test_b_or_t_appcond():
    a,b,c,d = makeVars("a","b","c","d")
    A = Seq([Or(a,b),c],FF())
    B = Seq([Or(a,b),Or(a,c)],FF())
    C = Seq([a,b],d)
    D = Seq([Or(a,c)],b)
    assert b_or_t_appcond([Or(a,b)],A) == True
    assert b_or_t_appcond([Or(a,c)],B) == True

    assert b_or_t_appcond([Or(a,b)],C) == False #pas de or
    assert b_or_t_appcond([Or(a,b)],D) == False #pas le bon or

test_b_or_t_appcond()