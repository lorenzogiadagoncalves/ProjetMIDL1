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

def b_or_t_appcond(fs: list[Form], s: Seq) -> bool:
    """
    fonction qui teste les condition d'applicabilité de la règle beta_or de
    la méthode des tableaux sur la ou les formules fs des hypothèse du séquent s
    entree : list[Form], s      la liste des formules sur lesquelles on veux agir, le sequent
    sortie : bool               si la condition d'applicabilité est valide ou non
    """
    match(fs,s):
        case ([Or(a,b)],Seq(g,FF())):
            return ((a not in g) and (b not in g))
        case _:
            return False

def b_or_t_action(fs: list[Form], s: Seq) -> list[Seq]:
    """
    fonction qui applique la règle beta_or de la méthode des tableaux en appliquant 
    cette règle sur la ou les formules de fs des hypothèses du séquent s
    entree : list[Form], s      la liste des formules sur lesquelles on veux agir, le sequent
    sortie : list[Seq]          la liste des sequent qui résultent de l'application de la règle
    """
    match(fs,s):
        case ([Or(a,b)],Seq(g,FF())):
            return ([Seq(g+[a],FF()),Seq(g+[b],FF())])
        case _:
            return ([])

b_or_t_rule = Rule("b_or_t", b_or_t_appcond, b_or_t_action)