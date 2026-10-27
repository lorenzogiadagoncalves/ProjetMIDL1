from datastructs import *
from rules import *
from tests import *

def next_proof_state(ps: ProofStateV0) -> list[ProofStateV0]:
    seq = ps[0] #on sait que ps est non vide sinon on aurait une preuve
    othersSeq = ps[1:len(ps)]

    listProofState = []
    for i in range(len(seq.hyps)):
        print("bcl 1",seq.hyps[i])
        for rule in [a_or_t_rule,b_or_t_rule]:
            print("bcl 2",rule.rulename)
            if rule.appcond([seq.hyps[i]],seq):
                print("testé ?")
                listSeq = rule.action([seq.hyps[i]],seq)
                print("listeSeq : ",listSeq)
                for newSeq in listSeq:
                    if newSeq != []:
                        print("nouveau : ",[newSeq] + othersSeq)
                        listProofState.append([newSeq] + othersSeq)
                break #je préfèrerais autre chose mais ça enleverais l'alias "rules" qui est très pratique
    return listProofState

