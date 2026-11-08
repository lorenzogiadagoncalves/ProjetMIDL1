# Projet MIDL 1

## Groupe

MONTAUT Tom

DUVOISIN Hector

GIADA GONCALVES Lorenzo

## Comment utiliser ?

> [!TIP]
> Pour faciliter la création de variables propositionelles, nous avons créé la fonction `makeVars()` dans [tests.py](tests.py) qui s'occupe de créer des variables pour chaque entrée.
> Exemple :
>
> ```py
> a, b, c, d = makeVars("a", "b", "c", "d")
> ```

Après la création d'un séquent, utilisez la fonction `prove_seq()` de [proof.py](proof.py) pour le prouver.

Pour exécuter les tests individuels sur les règles et quelques autres fonctions, lancez le fichier [tests.py](tests.py).

> [!NOTE]
> Nous avons utilisé la librairie standard [`unittest`](https://docs.python.org/3/library/unittest.html) pour tester nos fonctions.
