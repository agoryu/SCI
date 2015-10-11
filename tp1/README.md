TPs de SCI
==========

### Auteurs

- Elliot VANEGUE
- Gaëtan DEFLANDRE

### Dépendance

L'installation du packet **python3-tk** est nécessaire.



TP1: Simulation bille 
---------------------

### Bref

Plateau contenant des agents billes. Une boucle de décision est
effectuée pour chaque bille, pour déterminer leurs directions.


### Utilisation

    $ python3.4 main.py x y cellSize sleep nbBall isToric

- x : taille de l'environnement en x
- y : taille de l'environnement en y
- cellSize : hauteur et largeur de la bille carrée
- sleep : temps d'arrêt entre chaque tour en ms
- nbBall : nombre de billes
- isToric : environnement torique ou non (True/False)

Exemple:
    $ python3.4 main.py 100 100 8 50 200 True

Le bouton *start* lance la simulation pour 1000 tours. Après 1000
tours on peut continuer avec le bouton *start*.


### Détails

Lorsqu'une bille en percute une autre, seule la bille courante
rebondit. L'autre continue son chemin si elle peut. (méthode decide)



TP2: Simulation poission
------------------------

### Bref

Plateau contenant des agents pouvant être des requins ou des thons.
Les agents recherchent à survivre par différentes actions. Une
action par tour est choisie par la méthode *decide*.


### Utilisation

    $ python3.4 main2.py x y cellSize sleep nbAgent isToric

Les arguments sont identiques à ceux du TP1.

Configurations fonctionnelles:
```
    $ python3.4 main2.py 100 100 8 0 2000 True #Optimal
    $ python3.4 main2.py 50 50 8 0 400 True
```

Le bouton *start* lance la simulation pour 1000 tours. Après 1000
tours on peut continuer avec le bouton *start*.
Pour fermer la fenêtre de simulation, veuillez effectuer un CTRL+c
et cliquer sur la croix de la fenêtre.

### Caractéristiques

#### Thon
- reproduction: 10 tours

#### Requin
- reproduction: 10 tours
- mort de faim: 6 tours sans manger


### Détails

Quota : 1/10 de requin et 9/10 de poisson

Les poissons cherchent à survivre en fuyant les requins. Lorsqu'ils
en détecte un autour d'eux, ils partent dans la direction opposée.

Les requins quant à eux mangent les poissons qui se situent autours
d'eux. Lorsqu'un requin mange un poisson il se reproduit plus vite.

### Résultats

- égalité entre les requins et les poissons avec les premiers
  paramètres que nous avons fourni.
- victoire des poissons dans la majorité des cas lorsqu'on change les
  paramètres.
- les requins n'ont aucune chance de victoire excepté en modifiant le
  quota de poisson et de requin.



TP3: Hunter/Hunted
------------------

### Utilisation

    $ python3.4 main3.py x y cellSize sleep nbHunter nbHunted nbWall

- x : taille de l'environnement en x
- y : taille de l'environnement en y
- cellSize : hauteur et largeur de la bille carrée
- sleep : temps d'arrêt entre chaque tour en ms
- nbHunter : nombre d'agent Hunter
- nbHunted : nombre d'agent Hunted
- nbWall : nombre d'agent Wall, les murs

Exemple:
```
    $ python3.4 main3.py 80 80 10 0 2 1 100
    $ python3.4 main3.py 80 80 10 0 1 3 100
```
