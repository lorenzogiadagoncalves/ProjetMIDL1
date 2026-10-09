from datastructs import *

def allVars(f: Form) -> set[Var]:
    """
    Liste les variables d'une formule sans duplicat
    """
    return list(set(allVars_r(f)))


def allVars_r(f: Form) -> list[Var]:
    """
    Liste les variables d'une formule
    """
    match f:
        case FF():
            return []
        case Not(a):
            return allVars_r(a)
        case And(a,b):
            return allVars_r(a) + allVars_r(b)
        case Or(a,b):
            return allVars_r(a) + allVars_r(b)
        case Impl(a,b):
            return allVars_r(a) + allVars_r(b)
        case f:
            return [f]

def a_or_t_appcond(fs: list[Form], s: Seq) -> bool:
    match (fs, s):
        case ([Not(Or(a, b))], Seq(g, FF())):
            return not (Not(a) in g and Not(b) in g)
        case _:
            return False

def a_or_t_action(fs: list[Form], s: Seq) -> list[Seq]:
    match (fs, s):
        case ([Not(Or(a, b))], Seq(g, FF())):
            return [Seq(g + [Not(a), Not(b)], FF())]
        case _:
            return []

a_or_t_rule = Rule("a_or_t", a_or_t_appcond, a_or_t_action)
