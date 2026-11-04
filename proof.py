from datastructs import *
from rules import *
from typing import TypeVar

def next_proof_state(ps: ProofStateV0) -> list[ProofStateV0]:
    seq = ps[0] #on sait que ps est non vide sinon on aurait une preuve
    othersSeq = ps[1:len(ps)]

    rules = [a_or_t_rule,b_or_t_rule,a_and_t_rule,b_and_t_rule,a_impl_t_rule,b_impl_t_rule,a_x_c_rule,a_x_f_rule,start_rule]

    listProofState = []
    for i in range(len(seq.hyps)):
        print("bcl 1",seq.hyps[i])
        for rule in rules:
            print("bcl 2 "+rule.rulename)
            if rule.appcond([seq.hyps[i]],seq):
                print("testé ?")
                print("avant :",seq)
                listSeq = rule.action([seq.hyps[i]],seq)
                print("listeSeq : [")
                for a in listSeq:
                    print(a,",")
                print("]")
                for newSeq in listSeq:
                    if newSeq != []:
                        print("nouveau : ",newSeq)
                        listProofState.append([newSeq] + othersSeq)
                    else:
                        listProofState.append(othersSeq)
    print("listeProof finie")
    return listProofState

PS = TypeVar("PS")
def dfs (nexts: Callable[[PS], list[PS]],
    sol: Callable[[PS], bool],
    states: list[PS]) -> list[PS]:
    if states == []:
        return ([])
    else:
        if sol(states[0]):
            return [states [0]]
            # si vous souhaitez continuer la recherche , decommentez :
            # return [states [0]] + dfs(nexts , sol , nexts(states [0]) + states [1:])
        else:
            return dfs(nexts , sol , nexts(states [0]) + states [1:])

def sol_proof_state(states0: PS) -> bool:
    print("states0 :",states0)
    return states0 == []

def init_state(seq: Seq) -> list[ProofStateV0]:
    return [[seq]]

def prove_seq(sq: Seq) -> list[ ProofState ]:
    return dfs(next_proof_state , sol_proof_state , init_state(sq))