from dataclasses import dataclass
from typing import Callable, Union


# ---------------------------------------------------------------------------
# Form
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class FF:
    def __str__(self):
        return "⊥"


@dataclass(frozen=True)
class Var:
    name: str
    def __str__(self):
        return f"{self.name}"


@dataclass(frozen=True)
class Not:
    form: "Form"
    def __str__(self):
        return f"¬{self.form}"

@dataclass(frozen=True)
class And:
    left: "Form"
    right: "Form"
    def __str__(self):
        return f"({self.left} ∧ {self.right})"

@dataclass(frozen=True)
class Or:
    left: "Form"
    right: "Form"
    def __str__(self):
        return f"({self.left} ∨ {self.right})"


@dataclass(frozen=True)
class Impl:
    left: "Form"
    right: "Form"
    def __str__(self):
        return f"({self.left} → {self.right})"


Form = Union[
    FF,
    Var,
    Not,
    And,
    Or,
    Impl,
]


# ---------------------------------------------------------------------------
# Sequent
# ---------------------------------------------------------------------------


def hyps_in_str(list):
    hyps_str = ""
    for i in range (len(list)-1):
        hyps_str += str(list[i]) + ", "
    hyps_str += str(list[len(list)-1])
    return hyps_str


@dataclass(frozen=True)
class Seq:
    hyps: list[Form]
    concl: Form
    def __str__(self):
        return f"{hyps_in_str(self.hyps)} ⊢ {self.concl}"


# ---------------------------------------------------------------------------
# Rule-related types
# ---------------------------------------------------------------------------

Rulename = str

Appcond = Callable[[list[Form], Seq], bool]
Action = Callable[[list[Form], Seq], list[Seq]]


@dataclass(frozen=True)
class Rule:
    rulename: Rulename
    appcond: Appcond
    action: Action


Calculus = list[Rule]


# ---------------------------------------------------------------------------
# History
# ---------------------------------------------------------------------------

History = list[int]


# ---------------------------------------------------------------------------
# Goal
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class OpenGoal:
    history: History
    seq: Seq


@dataclass(frozen=True)
class ClosedGoal:
    history: History
    seq: Seq
    rulename: Rulename
    forms: list[Form]


# ---------------------------------------------------------------------------
# Proof state
# ---------------------------------------------------------------------------

ProofStateV0 = list[Seq]

# Proof state composed of list of open and closed goals
ProofState = tuple[list[OpenGoal], list[ClosedGoal]]


# ---------------------------------------------------------------------------
# Derivation
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class Deriv:
    seq: Seq
    rulename: Rulename
    forms: list[Form]
    children: list["Deriv"]
