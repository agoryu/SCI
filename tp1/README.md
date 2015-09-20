TP1: Agents billes
==================

## Bref

Plateau contenant des agents billes. Une boucle de décision est
effectuée pour chaque bille, pour déterminer leurs directions.


## Dépendance

L'installation du packet **python3-tk** est nécessaire


## Utilisation

    $ python3.4 main.py x y cellSize speed nbBall isToric

- x : taille de l'environnement en x
- y : taille de l'environnement en y
- cellSize : hauteur et largeur de la bille carré
- speed : ralentisseur
- nbBall : nombre de billes
- isToric : environnement torique ou non

### Exemple

    $ python3.4 main.py 500 500 2 1000 10000 true
