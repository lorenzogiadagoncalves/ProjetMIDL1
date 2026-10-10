from datastructs import *

def b_or_t_appcond(fs: list[Form], s: Seq) -> bool:
    match(fs,s):
        case ([Or(a,b)],Seq(g,FF())):
            return ((a not in g) and (b not in g))
        case _:
            return False

def b_or_t_action(fs: list[Form], s: Seq) -> list[Seq]:
    match(fs,s):
        case ([Or(a,b)],Seq(g,FF())):
            return ([Seq(g+[a],FF()),Seq(g+[b],FF())])
        case _:
            return ([])