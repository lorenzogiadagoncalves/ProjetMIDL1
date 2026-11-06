from typing import TypeVar

from datastructs import *
from rules import *

# FONCTIONS GÉNÉRALES
PS = TypeVar("PS")

def dfs(
    nexts: Callable[[PS], list[PS]], sol: Callable[[PS], bool], states: list[PS]
) -> list[PS]:
    """
    Cherche une solution à une liste d'états.

    Paramètres :
        nexts (PS -> list[PS]) : fonction qui dérive de nouveaux états depuis un état donné.
        sol (PS -> bool) : fonction qui détermine si un état est solution.
        states (list[PS]) : liste des états de départ.

    Retourne :
        Une liste d'états solution des états de départ.
    """

    if states == []:
        return []

    else:
        if sol(states[0]):
            return [states[0]]
            # si vous souhaitez continuer la recherche , decommentez :
            # return [states [0]] + dfs(nexts , sol , nexts(states [0]) + states [1:])
        else:
            return dfs(nexts, sol, nexts(states[0]) + states[1:])

# RECHERCHE DE PREUVE DANS LE CALCUL T
def next_proof_state(ps: ProofStateV0) -> list[ProofStateV0]:
    """
    Dérive tous les séquents possibles à partir des séquents donnés dans le
    calcul T.

    Paramètres :
        ps (ProofStateV0) : liste des séquents de départ ; ou l'état de la
            recherche de preuve.

    Retourne :
        La liste des listes des séquents dérivés, une par séquent de départ.
    """
    # TODO: enlever les prints ?

    seq = ps[0] # on sait que ps est non vide sinon on aurait une preuve
    othersSeq = ps[1 : len(ps)]

    listProofState = []

    for i in range(len(seq.hyps)):
        print("bcl 1", seq.hyps[i])

        for rule in rules:
            print("bcl 2 " + rule.rulename)

            if rule.appcond([seq.hyps[i]], seq):
                print("testé ?")
                print("avant :", seq)

                listSeq = rule.action([seq.hyps[i]], seq)

                print("listeSeq : [")
                for a in listSeq:
                    print(a, ",")
                print("]")

                for newSeq in listSeq:
                    if newSeq != []:
                        print("nouveau : ", newSeq)
                        listProofState.append([newSeq] + othersSeq)

                    else:
                        listProofState.append(othersSeq)

    print("listeProof finie")
    return listProofState

def sol_proof_state(state: ProofStateV0) -> bool:
    """
    Détermine si un état est solution dans le calcul T.

    Paramètres :
        state (ProofStateV0) : l'état à vérifier.

    Retourne :
        True si state est solution, False sinon.
    """

    return state == []


def init_state(seq: Seq) -> list[ProofStateV0]:
    """
    Construit un état de recherche de preuve de départ à partir d'un séquent.

    Paramètres :
        seq (Seq) : le séquent de départ.

    Retourne :
        Le même séquent, sous forme d'état de recherche de preuve.
    """

    return [[seq]]


def prove_seq(sq: Seq) -> list[ProofState]:
    """
    Prouve un séquent dans le calcul T.

    Paramètres :
        sq (Seq) : le séquent à prouver.

    Retourne :
        [] si le séquent n'est pas prouvable, [[]] sinon.
    """

    return dfs(next_proof_state, sol_proof_state, init_state(sq))
