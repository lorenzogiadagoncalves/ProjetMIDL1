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