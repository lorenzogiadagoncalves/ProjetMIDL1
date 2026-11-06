from datastructs import *


# UTILITAIRES
def allVars(f: Form) -> set[Var]:
    """
    Liste les variables d'une formule sans duplicatas.

    Paramètres :
        f (Form) : la formule à analyser.

    Retourne :
        Un ensemble contenant les variables utilisées dans la formule f.
    """

    return list(set(allVars_r(f)))


def allVars_r(f: Form) -> list[Var]:
    """
    Liste les variables d'une formule (avec duplicatas).

    Paramètres :
        f (Form) : la formule à analyser.

    Retourne :
        Une liste contenant les variables utilisées dans la formule f.
    """

    match f:
        case FF():
            return []
        case Not(a):
            return allVars_r(a)
        case And(a, b):
            return allVars_r(a) + allVars_r(b)
        case Or(a, b):
            return allVars_r(a) + allVars_r(b)
        case Impl(a, b):
            return allVars_r(a) + allVars_r(b)
        case f:
            return [f]


# RÈGLES
## Règle Start (S). TODO
def start_t_appcond(fs: list[Form], s: Seq) -> bool:
    """
    Teste l'applicabilité de la règle Start (S).

    Paramètres :
        fs (list[Form]) : les formules sur lesquelles on veut agir.
        s (Seq) : le séquent.

    Retourne :
        True si la règle est applicable, False sinon.
    """

    match (fs, s):
        case ([], Seq(g, b)):
            return not (Not(b) in g)
        case _:
            return False


def start_t_action(fs: list[Form], s: Seq) -> list[Seq]:
    """
    Applique la règle Start (S) aux formules données.

    Paramètres :
        fs (list[Form]) : les formules sur lesquelles on veut agir.
        s (Seq) : le séquent.

    Retourne :
        Les séquents dérivés de la règle.
    """

    match (fs, s):
        case ([], Seq(g, b)):
            return [Seq(g + [b], FF())]
        case _:
            return []


start_t_rule = Rule("start_t", start_t_appcond, start_t_action)


## Axiome n°1 (AxF)
def ax_f_t_appcond(fs: list[Form], s: Seq) -> bool:
    """
    Teste l'applicabilité de l'axiome n°1 (AxF).

    Paramètres :
        fs (list[Form]) : les formules sur lesquelles on veut agir.
        s (Seq) : le séquent.

    Retourne :
        True si la règle est applicable, False sinon.
    """

    match (fs, s):
        case ([FF()], Seq(g, FF())):
            return True
        case _:
            return False


def ax_f_t_action(fs: list[Form], s: Seq) -> list[Seq]:
    """
    Applique l'axiome n°1 (AxF) aux formules données.

    Paramètres :
        fs (list[Form]) : les formules sur lesquelles on veut agir.
        s (Seq) : le séquent.

    Retourne :
        Les séquents dérivés de la règle.
    """

    match (fs, s):
        case ([FF()], Seq(g, FF())):
            return []
        case _:
            return []


ax_f_t_rule = Rule("ax_f_t", ax_f_t_appcond, ax_f_t_action)


## Axiome n°2 (AxC)
def ax_c_t_appcond(fs: list[Form], s: Seq) -> bool:
    """
    Teste l'applicabilité de l'axiome n°2 (AxC).

    Paramètres :
        fs (list[Form]) : les formules sur lesquelles on veut agir.
        s (Seq) : le séquent.

    Retourne :
        True si la règle est applicable, False sinon.
    """

    match (fs, s):
        case ([a], Seq(g, FF())):
            return Not(a) in g
        case _:
            return False


def ax_c_t_action(fs: list[Form], s: Seq) -> list[Seq]:
    """
    Applique l'axiome n°2 (AxC) aux formules données.

    Paramètres :
        fs (list[Form]) : les formules sur lesquelles on veut agir.
        s (Seq) : le séquent.

    Retourne :
        Les séquents dérivés de la règle.
    """

    match (fs, s):
        case ([a], Seq(g, FF())):
            return []
        case _:
            return []


ax_c_t_rule = Rule("ax_c_t", ax_c_t_appcond, ax_c_t_action)


## Règle de la négation (N)
def n_t_appcond(fs: list[Form], s: Seq) -> bool:
    """
    Teste l'applicabilité de la règle de la négation (N).

    Paramètres :
        fs (list[Form]) : les formules sur lesquelles on veut agir.
        s (Seq) : le séquent.

    Retourne :
        True si la règle est applicable, False sinon.
    """

    match (fs, s):
        case ([Not(Not(a))], Seq(g, FF())):
            return a not in g
        case _:
            return False


def n_t_action(fs: list[Form], s: Seq) -> list[Seq]:
    """
    Applique la règle de la négation (N) aux formules données.

    Paramètres :
        fs (list[Form]) : les formules sur lesquelles on veut agir.
        s (Seq) : le séquent.

    Retourne :
        Les séquents dérivés de la règle.
    """

    match (fs, s):
        case ([Not(Not(a))], Seq(g, FF())):
            return [Seq(g + [a], FF())]
        case _:
            return []


n_t_rule = Rule("n_t", n_t_appcond, n_t_action)


## Règle (α∧)
def a_and_t_appcond(fs: list[Form], s: Seq) -> bool:
    """
    Teste l'applicabilité de la règle (α∧).

    Paramètres :
        fs (list[Form]) : les formules sur lesquelles on veut agir.
        s (Seq) : le séquent.

    Retourne :
        True si la règle est applicable, False sinon.
    """

    match (fs, s):
        case ([And(a, b)], Seq(g, FF())):
            return (a not in g) or (b not in g)
        case _:
            return False


def a_and_t_action(fs: list[Form], s: Seq) -> list[Seq]:
    """
    Applique la règle (α∧) aux formules données.

    Paramètres :
        fs (list[Form]) : les formules sur lesquelles on veut agir.
        s (Seq) : le séquent.

    Retourne :
        Les séquents dérivés de la règle.
    """

    match (fs, s):
        case ([And(a, b)], Seq(g, FF())):
            return [
                Seq(g + ([a] if a not in g else []) + [b] if b not in g else [], FF())
            ]
        case _:
            return []


a_and_t_rule = Rule("a_and_t", a_and_t_appcond, a_and_t_action)


## Règle (β∧)
def b_and_t_appcond(fs: list[Form], s: Seq) -> bool:
    """
    Teste l'applicabilité de la règle (β∧).

    Paramètres :
        fs (list[Form]) : les formules sur lesquelles on veut agir.
        s (Seq) : le séquent.

    Retourne :
        True si la règle est applicable, False sinon.
    """

    match (fs, s):
        case ([And(a, b)], Seq(g, FF())):
            return (Not(a) not in g) or (Not(b) not in g)
        case _:
            return False


def b_and_t_action(fs: list[Form], s: Seq) -> list[Seq]:
    """
    Applique la règle (β∧) aux formules données.

    Paramètres :
        fs (list[Form]) : les formules sur lesquelles on veut agir.
        s (Seq) : le séquent.

    Retourne :
        Les séquents dérivés de la règle.
    """

    match (fs, s):
        case ([And(a, b)], Seq(g, FF())):
            return [Seq(g + [Not(a)], FF()), Seq(g + [Not(b)], FF())]
        case _:
            return []


b_and_t_rule = Rule("b_and_t", b_and_t_appcond, b_and_t_action)


## Règle (α∨)
def a_or_t_appcond(fs: list[Form], s: Seq) -> bool:
    """
    Teste l'applicabilité de la règle (α∨).

    Paramètres :
        fs (list[Form]) : les formules sur lesquelles on veut agir.
        s (Seq) : le séquent.

    Retourne :
        True si la règle est applicable, False sinon.
    """

    match (fs, s):
        case ([Not(Or(a, b))], Seq(g, FF())):
            return not (Not(a) in g and Not(b) in g)
        case _:
            return False


def a_or_t_action(fs: list[Form], s: Seq) -> list[Seq]:
    """
    Applique la règle (α∨) aux formules données.

    Paramètres :
        fs (list[Form]) : les formules sur lesquelles on veut agir.
        s (Seq) : le séquent.

    Retourne :
        Les séquents dérivés de la règle.
    """

    match (fs, s):
        case ([Not(Or(a, b))], Seq(g, FF())):
            return [Seq(g + [Not(a), Not(b)], FF())]
        case _:
            return []


a_or_t_rule = Rule("a_or_t", a_or_t_appcond, a_or_t_action)


## Règle (β∨)
def b_or_t_appcond(fs: list[Form], s: Seq) -> bool:
    """
    Teste l'applicabilité de la règle (β∨).

    Paramètres :
        fs (list[Form]) : les formules sur lesquelles on veut agir.
        s (Seq) : le séquent.

    Retourne :
        True si la règle est applicable, False sinon.
    """

    match (fs, s):
        case ([Or(a, b)], Seq(g, FF())):
            return (a not in g) or (b not in g)
        case _:
            return False


def b_or_t_action(fs: list[Form], s: Seq) -> list[Seq]:
    """
    Applique la règle (β∨) aux formules données.

    Paramètres :
        fs (list[Form]) : les formules sur lesquelles on veut agir.
        s (Seq) : le séquent.

    Retourne :
        Les séquents dérivés de la règle.
    """

    match (fs, s):
        case ([Or(a, b)], Seq(g, FF())):
            return [Seq(g + [a], FF()), Seq(g + [b], FF())]
        case _:
            return []


b_or_t_rule = Rule("b_or_t", b_or_t_appcond, b_or_t_action)


## Règle (α→)
def a_impl_t_appcond(fs: list[Form], s: Seq) -> bool:
    """
    Teste l'applicabilité de la règle (α→).

    Paramètres :
        fs (list[Form]) : les formules sur lesquelles on veut agir.
        s (Seq) : le séquent.

    Retourne :
        True si la règle est applicable, False sinon.
    """

    match (fs, s):
        case ([Not(Impl(a, b))], Seq(g, FF())):
            return a not in g or Not(b) not in g
        case _:
            return False


def a_impl_t_action(fs: list[Form], s: Seq) -> list[Seq]:
    """
    Applique la règle (α→) aux formules données.

    Paramètres :
        fs (list[Form]) : les formules sur lesquelles on veut agir.
        s (Seq) : le séquent.

    Retourne :
        Les séquents dérivés de la règle.
    """

    match (fs, s):
        case ([Not(Impl(a, b))], Seq(g, FF())):
            return [Seq(g + [a, Not(b)], FF())]
        case _:
            return []


a_impl_t_rule = Rule("a_impl_t", a_impl_t_appcond, a_impl_t_action)


## Règle (β→)
def b_impl_t_appcond(fs: list[Form], s: Seq) -> bool:
    """
    Teste l'applicabilité de la règle (β→).

    Paramètres :
        fs (list[Form]) : les formules sur lesquelles on veut agir.
        s (Seq) : le séquent.

    Retourne :
        True si la règle est applicable, False sinon.
    """

    match (fs, s):
        case ([Impl(a, b)], Seq(g, FF())):
            return Not(a) not in g or b not in g
        case _:
            return False


def b_impl_t_action(fs: list[Form], s: Seq) -> list[Seq]:
    """
    Applique la règle (β→) aux formules données.

    Paramètres :
        fs (list[Form]) : les formules sur lesquelles on veut agir.
        s (Seq) : le séquent.

    Retourne :
        Les séquents dérivés de la règle.
    """

    match (fs, s):
        case ([Impl(a, b)], Seq(g, FF())):
            return [Seq(g + [Not(a)], FF()), Seq(g + [b], FF())]
        case _:
            return []


b_impl_t_rule = Rule("b_impl_t", b_impl_t_appcond, b_impl_t_action)

rules = [
    start_t_rule,
    ax_f_t_rule,
    ax_c_t_rule,
    n_t_rule,
    a_and_t_rule,
    b_and_t_rule,
    a_or_t_rule,
    b_or_t_rule,
    a_impl_t_rule,
    b_impl_t_rule,
]
