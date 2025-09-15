<p align="center">
<img src="https://github.com/Mathieu7483/Aiko78-Photgraphy/blob/main/img/python%20n%C3%A9eon%20carte%20%C3%A9l%C3%A9ctronique.png">
</p>

# 0x09. Python - More Classes and Objects
# 📝 Description

Ce projet approfondit les concepts de la Programmation Orientée Objet (POO) en Python. En se basant sur une classe Rectangle, il introduit des notions avancées comme les attributs de classe pour compter les instances, la redéfinition d'opérateurs (__str__, __repr__, __del__) pour une meilleure représentation et gestion des objets, l'utilisation de méthodes statiques et de classe pour des fonctionnalités liées à la classe elle-même, et la possibilité d'utiliser eval() pour recréer une instance à partir de sa représentation.

# 📂 Contenu de l'exercice

Ce répertoire contient les fichiers source des classes, chacun correspondant à une étape progressive de l'apprentissage des concepts de la POO.

[0-rectangle.py](): Une classe Rectangle vide.

[1-rectangle.py](): Définition du rectangle avec des attributs privés __width et __height et leurs propriétés associées pour la validation.

[2-rectangle.py](): Ajout des méthodes d'instance publiques area() et perimeter().

[3-rectangle.py](): Implémentation de la représentation du rectangle avec print() et str().

[4-rectangle.py](): Ajout de la représentation "officielle" de l'objet via repr(), permettant de le recréer avec eval().

[5-rectangle.py](): Utilisation du destructeur __del__ pour imprimer un message lors de la suppression d'une instance.

[6-rectangle.py](): Introduction d'un attribut de classe public number_of_instances pour compter le nombre d'instances créées et supprimées.

[7-rectangle.py](): Ajout d'un attribut de classe print_symbol pour personnaliser le caractère d'affichage du rectangle.

[8-rectangle.py](): Création d'une méthode statique bigger_or_equal() pour comparer deux rectangles.

[9-rectangle.py](): Création d'une méthode de classe square() pour instancier un carré.

# 🛠️ Prérequis

Environnement : Ubuntu 20.04 LTS

Interpréteur : Python 3.8.5

Ligne de code : Chaque fichier Python doit commencer par #!/usr/bin/python3

Formatage : Le code doit respecter les règles de pycodestyle (version 2.7.*)

# 🚀 Tests

Pour tester les fichiers, exécutez le script main fourni pour chaque tâche. Par exemple, pour la tâche 0 :

```Bash

./0-main.py
```
# ✍️ Auteur
[Mathieu GODALIER](https://github.com/Mathieu7483) - Élève en programmation à la Holberton School

# ⚖️ Licence

Ce projet est sous licence MIT. Pour plus de détails, consultez le fichier LICENSE.

# 🙏 Remerciements

Ce projet a été réalisé dans le cadre du cursus de programmation de l'École Holberton. Un grand merci pour l'opportunité d'apprendre les bases de la POO en Python.