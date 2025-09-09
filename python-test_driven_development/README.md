<p align="center">
<img src=https://github.com/Mathieu7483/Aiko78-Photgraphy/blob/main/img/python%20n%C3%A9eon%20carte%20%C3%A9l%C3%A9ctronique.png>
</p>

# 0x04. Python - Test-driven development

# 📝 Description

Ce projet met en pratique le développement piloté par les tests (TDD) en Python. L'objectif est de s'habituer à écrire les tests et la documentation des fonctions avant de commencer à écrire le code. Les exercices couvrent la création de tests interactifs en utilisant la syntaxe doctest directement dans les docstrings, ainsi que l'utilisation du module unittest pour des tests plus structurés. Le projet insiste sur l'importance de couvrir tous les cas d'usage, y compris les cas limites (edge cases).

# 📂 Contenu de l'exercice

Ce répertoire contient les fichiers source des fonctions et les fichiers de tests correspondants.

0-add_integer.py : Une fonction qui additionne deux entiers, avec ses tests dans tests/0-add_integer.txt.

2-matrix_divided.py : Une fonction qui divise tous les éléments d'une matrice, avec ses tests dans tests/2-matrix_divided.txt.

3-say_my_name.py : Une fonction qui imprime un nom et un prénom, avec ses tests dans tests/3-say_my_name.txt.

4-print_square.py : Une fonction qui imprime un carré de #, avec ses tests dans tests/4-print_square.txt.

5-text_indentation.py : Une fonction qui met en forme un texte en ajoutant des sauts de ligne, avec ses tests dans tests/5-text_indentation.txt.

6-max_integer.py : Une fonction qui trouve le plus grand entier dans une liste.

tests/6-max_integer_test.py : Les tests unitaires pour la fonction max_integer.

# 🛠️ Prérequis

Environnement : Ubuntu 20.04 LTS

Interpréteur : Python 3.8.5

Ligne de code : Chaque fichier Python doit commencer par #!/usr/bin/python3

Formatage : Le code doit respecter les règles de pycodestyle (version 2.7.*)

# 🚀 Tests

Les tests de ce projet sont de deux types :

Doctests : Pour exécuter les tests intégrés dans les docstrings, utilisez la commande suivante depuis le répertoire parent :

```Bash

python3 -m doctest ./tests/*.txt
```
Unittests : Pour exécuter les tests unitaires pour le fichier 6-max_integer.py, utilisez la commande suivante depuis le répertoire parent :

````Bash

python3 -m unittest tests/6-max_integer_test.py
````

# ✍️ Auteur
[Mathieu GODALIER](https://github.com/Mathieu7483) - Élève en programmation à la Holberton School


# ⚖️ Licence

Ce projet est sous licence MIT. Pour plus de détails, consultez le fichier LICENSE.

# 🙏 Remerciements

Ce projet a été réalisé dans le cadre du cursus de programmation de l'École Holberton. Un grand merci pour l'opportunité de maîtriser le développement piloté par les tests.