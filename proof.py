from typing import TypeVar

from datastructs import *
from rules import *


def next_proof_state(ps: ProofStateV0) -> list[ProofStateV0]:
    seq = ps[0]  # on sait que ps est non vide sinon on aurait une preuve
    othersSeq = ps[1 : len(ps)]

    listProofState = []
    for i in range(len(seq.hyps)):
        print("bcl 1", seq.hyps[i])
        for rule in rules:
            print("bcl 2", rule.rulename)
            if rule.appcond([seq.hyps[i]], seq):
                print("testé ?")
                listSeq = rule.action([seq.hyps[i]], seq)
                print("listeSeq : ", listSeq)
                for newSeq in listSeq:
                    if newSeq != []:
                        print("nouveau : ", [newSeq] + othersSeq)
                        listProofState.append([newSeq] + othersSeq)
                break  # je préfèrerais autre chose mais ça enleverais l'alias "rules" qui est très pratique
    print("listeProof :", listProofState)
    return listProofState


PS = TypeVar("PS")


def dfs(
    nexts: Callable[[PS], list[PS]], sol: Callable[[PS], bool], states: list[PS]
) -> list[PS]:
    if states == []:
        return []
    else:
        if sol(states[0]):
            return [states[0]]
            # si vous souhaitez continuer la recherche , decommentez :
            # return [states [0]] + dfs(nexts , sol , nexts(states [0]) + states [1:])
        else:
            return dfs(nexts, sol, nexts(states[0]) + states[1:])


def sol_proof_state(states0: PS) -> bool:
    return states0 == []


def init_state(seq: Seq) -> list[ProofStateV0]:
    return [[seq]]


def prove_seq(sq: Seq) -> list[ProofState]:
    """
    Prouve un séquent à l'aide du calcul T.

    Paramètres :
        sq (Seq) : le séquent à prouver.

    Retourne :
        [] si le séquent n'est pas prouvable, [[]] sinon.
    """
    return dfs(next_proof_state, sol_proof_state, init_state(sq))
