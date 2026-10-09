from datastructs import *
from rules import b_or_t_appcond

"""fonction qui instancie une nombre x de variables propositionnelles"""
def makeVars(*vars):
    if len(vars) == 1:
        return Var(vars[0])
    return tuple([Var(var) for var in vars])


def test_b_or_t_appcond():
    a,b = makeVars("a","b")
    A = Seq([Or(Not(a),Not(b))],FF())
    assert b_or_t_appcond()
