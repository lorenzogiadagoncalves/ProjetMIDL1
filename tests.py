import unittest

from datastructs import *
from rules import *
from proof import *


# UTILITAIRES
def makeVars(*vars: list[str]):
    """
    Instancie n variables propositionnelles.

    Paramètres :
        *vars (list[str]) : toutes les variables à instancier.

    Retourne :
        Les mêmes variables que données en paramètres, enveloppées dans des Var.
    """

    if len(vars) == 1:
        return Var(vars[0])
    else:
        return tuple([Var(var) for var in vars])


# TESTS
## Règles
class TestRules(unittest.TestCase):
    def test_start_t(self):
        pass

    def test_ax_f_t(self):
        pass

    def test_ax_c_t(self):
        pass

    def test_n_t(self):
        pass

    def test_a_and_t(self):
        a, b, c, d = makeVars("a", "b", "c", "d")
        A = Seq([And(a, b), c], FF())
        B = Seq([And(a, b), Or(a, c)], FF())

        C = Seq([a, b], d)
        D = Seq([And(a, c), a, b], b)

        self.assertTrue(b_or_t_appcond([Or(a, b)], A))
        self.assertTrue(b_or_t_appcond([Or(a, c)], B))

        self.assertFalse(b_or_t_appcond([Or(a, b)], C))  # pas de or
        self.assertFalse(b_or_t_appcond([Or(a, b)], D))  # variables déjà présentes

    def test_b_and_t(self):
        pass

    def test_a_or_t(self):
        pass

    def test_b_or_t(self):
        a, b, c, d = makeVars("a", "b", "c", "d")
        A = Seq([Or(a, b), c], FF())
        B = Seq([Or(a, b), Or(a, c)], FF())

        C = Seq([a, b], d)
        D = Seq([Or(a, c)], b)

        self.assertTrue(b_or_t_appcond([Or(a, b)], A))
        self.assertTrue(b_or_t_appcond([Or(a, c)], B))

        self.assertFalse(b_or_t_appcond([Or(a, b)], C))  # pas de or
        self.assertFalse(b_or_t_appcond([Or(a, b)], D))  # pas le bon or

        self.assertEqual(
            b_or_t_action([Or(a, b)], A),
            [
                Seq([Or(a, b), c, a], FF()),
                Seq([Or(a, b), c, b], FF()),
            ],
        )
        self.assertEqual(
            b_or_t_action([Or(a, c)], B),
            [
                Seq([Or(a, b), Or(a, c), a], FF()),
                Seq([Or(a, b), Or(a, c), c], FF()),
            ],
        )

    def test_a_impl_t(self):
        pass

    def test_b_impl_t(self):
        pass


## Preuves
class TestProofs(unittest.TestCase):
    def test_prove_seq(self):
        a, b, c, d = makeVars("a", "b", "c", "d")

        # TODO: séquent d'exemple
        seq = Seq([a], a)

        self.assertEqual(prove_seq(seq), [[]])


if __name__ == "__main__":
    unittest.main()
