# Pokematon

Pokematon is a small python software to find the smallest non deterministic automaton corresponding to a DFA

## Install

Pokematon consists in one single python file: `pokematon.py`

In order to run it, you will need to install the project dependencies:
```
pip3 install -r requirements.txt
```

## Run tests

To run the tests, go to the root of the project and use command 
```
python3 -m unittest tests
```

## How it works (fr)

L'algorithme énumère tous les automates finis non-déterministes d'une certaine taille pour un certain alphabet.
Pour ce faire, plusieurs choses sont à considérer :
- *Les états finaux* : peu importe sur quel état ils se trouvent, vu qu'on ajoute les transitions après. La seule chose
importante est le nombre d'états finaux parmis tous les états de l'automate. On ne considère pas le cas sans états finaux
puisqu'il ne reconnait rien, il y a donc `n` cas à considérer.
- *L'état initial* : peut se trouver sur un état final, ou non. On a donc deux cas par combinaison d'états finaux, sauf quand
tous les états sont des états finaux. Ce qui porte le nombre d'automates à considérer à `2*n - 1`
- *Les symboles associés aux transitions* : il y a en tout `n^2` transitions dans l'automate. Pour une transition donnée,
chaque symbole peut être présent, ou non. Pour chaque transition il y a donc `2^k` possibilités. Au total on a `2^(k * n^2)`
configurations de transitions différentes

Nombre d'automates au total : `(2*n - 1) * 2^(k * n^2)`

Précisions :
- `n` est le nombre d'états
- `k` est la taille de l'alphabet