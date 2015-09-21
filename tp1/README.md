TP1: Agents billes
==================

## Bref

Plateau contenant des agents billes. Une boucle de décision est
effectuée pour chaque bille, pour déterminer leurs directions.


## Dépendance

L'installation du packet **python3-tk** est nécessaire.


## Utilisation

    $ python3.4 main.py x y cellSize sleep nbBall isToric

- x : taille de l'environnement en x
- y : taille de l'environnement en y
- cellSize : hauteur et largeur de la bille carrée
- sleep : temps d'arrêt entre chaque tour en ms
- nbBall : nombre de billes
- isToric : environnement torique ou non (True/False)

### Exemple

    $ python3.4 main.py 100 100 8 70 50 False

Le bouton *start* lance la simulation pour 1000 tours. Après 1000
tours on peut continuer avec le bouton *start*.
