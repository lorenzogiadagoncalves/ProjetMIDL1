from datastructs import *
from rules import *

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

def test_a_and_t_appcond():
    """
    fonction qui teste a_and_t_appcond
    """
    a,b,c,d = makeVars("a","b","c","d")
    A = Seq([And(a,b),c],FF())
    B = Seq([And(a,b),Or(a,c)],FF())

    C = Seq([a,b], d)
    D = Seq([And(a,c),a,b],b)

    assert b_or_t_appcond([Or(a,b)],A)
    assert b_or_t_appcond([Or(a,c)],B)

    assert not b_or_t_appcond([Or(a,b)],C) # pas de or
    assert not b_or_t_appcond([Or(a,b)],D) # variables déjà présentes


def test_a_and_t_action():
    pass

def test_b_and_t_appcond():
    pass

def test_b_and_t_action():
    pass

def test_n_t_appcond():
    pass

def test_n_t_action():
    pass

def test_a_impl_t_appcond():
    pass

def test_a_impl_t_action():
    pass

def test_b_impl_t_appcond():
    pass

def test_b_impl_t_action():
    pass
