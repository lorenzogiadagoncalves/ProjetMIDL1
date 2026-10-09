from datastructs import *

def b_or_t_appcond(fs: list[Form], s: Seq) -> bool:
    match(fs,s):
        #il ne faut pas avoir A et B déjà présents
        case ([Or(a,b)],Seq(_,FF())):
            return ((a not in s.hyps) and (b not in s.hyps))
        case _:
            return False