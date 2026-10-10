from datastructs import *

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