from datastructs import *

from rules import *


def makeVars(*vars:tuple[str]) -> tuple[Var]:
    """
    fonction qui instancie un nombre n de variables propositionnelles
    entree : tuple[str] les noms des variables à instancier
    sortie : tuple[var] les variables après instantiation
    """
    if len(vars) == 1:
        return Var(vars[0])
    return tuple([Var(var) for var in vars])


def test_b_or_t_appcond():
    """
    fonction qui teste b_or_t_appcond
    """
    a,b,c,d = makeVars("a","b","c","d")
    A = Seq([Or(a,b),c],FF())
    B = Seq([Or(a,b),Or(a,c)],FF())

    C = Seq([a,b],d)
    D = Seq([Or(a,c)],b)

    assert b_or_t_appcond([Or(a,b)],A) == True
    assert b_or_t_appcond([Or(a,c)],B) == True

    assert b_or_t_appcond([Or(a,b)],C) == False #pas de or
    assert b_or_t_appcond([Or(a,b)],D) == False #pas le bon or

def test_b_or_t_action():
    """
    fonction qui teste b_or_t_action
    """
    a,b,c,d = makeVars("a","b","c","d")
    A = Seq([Or(a,b),c],FF())
    B = Seq([Or(a,b),Or(a,c)],FF())

    assert b_or_t_action([Or(a,b)],A) == [Seq([Or(a,b),c,a],FF()),Seq([Or(a,b),c,b],FF())]
    assert b_or_t_action([Or(a,c)],B) == [Seq([Or(a,b),Or(a,c),a],FF()),Seq([Or(a,b),Or(a,c),c],FF())]
