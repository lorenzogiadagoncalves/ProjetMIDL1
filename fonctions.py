from datastructs import *

def a_or_t_appcond(fs: list[Form], s: Seq) -> bool:
    match (fs, s):
        case ([Not(Or(a, b))], Seq(g, FF())):
            # TODO: condition d'applicabilité étendue
            return True
        case _:
            return False

def a_or_t_action(fs: list[Form], s: Seq) -> list[Seq]:
    match (fs, s):
        case ([Not(Or(a, b))], Seq(g, FF())):
            return [Seq(g + [Not(a), Not(b)], FF())]
        case _:
            return []

a_or_t_rule = Rule("a_or_t", a_or_t_appcond, a_or_t_action)
