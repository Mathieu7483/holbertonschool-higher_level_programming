<p align="center">
<img src=https://github.com/Mathieu7483/Aiko78-Photgraphy/blob/main/img/python%20n%C3%A9eon%20carte%20%C3%A9l%C3%A9ctronique.png>
</p>

# 0x03. Python - Exceptions

# 📝 Description

Ce projet explore la gestion des erreurs et des exceptions en Python. L'objectif est de comprendre la différence entre les deux et d'apprendre à utiliser les blocs try, except, et finally pour créer un code plus fiable et résilient. Les exercices abordent la gestion des erreurs de type (TypeError), des erreurs d'index (IndexError), des divisions par zéro (ZeroDivisionError), ainsi que la levée d'exceptions personnalisées.

# 📂 Contenu de l'exercice

Ce répertoire contient les solutions des exercices du projet. Chaque fichier correspond à une tâche spécifique.

0-safe_print_list.py : Une fonction qui imprime en toute sécurité un nombre x d'éléments d'une liste.

1-safe_print_integer.py : Une fonction qui imprime un entier de manière sécurisée, gérant les valeurs non-entières.

2-safe_print_list_integers.py : Une fonction qui imprime uniquement les entiers d'une liste, en gérant les exceptions.

3-safe_print_division.py : Une fonction qui gère les divisions par zéro et s'assure d'imprimer un résultat dans le bloc finally.

4-list_division.py : Une fonction qui divise deux listes élément par élément, en gérant plusieurs types d'erreurs (type, division par zéro, et index hors de portée).

5-raise_exception.py : Une fonction qui lève une exception de type TypeError.

6-raise_exception_msg.py : Une fonction qui lève une exception de type NameError avec un message personnalisé.

7- 100-safe_print_integer_err.py : Cette fonction imprime un entier de manière sécurisée. Si la valeur n'est pas un entier, elle renvoie False et affiche le message d'erreur standard sur la sortie d'erreur (stderr), sans interrompre le programme.

8- 101-safe_function.py : Cette fonction exécute une autre fonction de manière sécurisée. Si une exception se produit pendant l'exécution, elle la gère, affiche l'erreur sur stderr et retourne None, permettant ainsi au programme de continuer son exécution sans planter.

9- 102-magic_calculation.py: Cette tâche consiste à reconstruire une fonction Python à partir de son bytecode. L'objectif est de traduire les instructions de bas niveau en code Python fonctionnel, comprenant les boucles, les opérations et la gestion des exceptions.

# 🛠️ Prérequis

Environnement : Ubuntu 20.04 LTS

Interpréteur : Python 3.8.5

Ligne de code : Chaque fichier Python doit commencer par #!/usr/bin/python3

Formatage : Le code doit respecter les règles de pycodestyle (version 2.7.*)

# 🚀 Compilation et exécution

Pour exécuter les scripts, assurez-vous que les fichiers sont exécutables (chmod +x <nom_du_fichier.py>).

Exemple pour le fichier 0-main.py :

```Bash

./0-main.py
```

# ✍️ Auteur
[Mathieu GODALIER](https://github.com/Mathieu7483) - Élève en programmation à la Holberton School

# ⚖️ Licence

Ce projet est sous licence MIT. Pour plus de détails, consultez le fichier LICENSE.

# 🙏 Remerciements

Ce projet a été réalisé dans le cadre du cursus de programmation de l'École Holberton. Un grand merci pour l'opportunité d'approfondir ma compréhension des exceptions en Python.