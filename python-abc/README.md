<p align="center">
<img src="https://github.com/Mathieu7483/Aiko78-Photgraphy/blob/main/img/python%20n%C3%A9eon%20carte%20%C3%A9l%C3%A9ctronique.png">
</p>

# 0x0B. Python - Abstract Classes and Interfaces
# 📝 Description

Ce projet explore des concepts avancés de la Programmation Orientée Objet (POO) en Python, notamment les classes abstraites, les interfaces, le "duck typing" et l'héritage multiple. Il montre comment utiliser ces principes pour concevoir des structures de code flexibles, modulaires et réutilisables. Les exercices progressent de la mise en place de bases abstraites à l'extension des classes natives et à la composition de comportements complexes via des "mixins".

# 📂 Contenu de l'exercice

Chaque fichier de ce répertoire représente une tâche progressive qui illustre un concept clé de la POO.

[task_00_abc.py](https://github.com/Mathieu7483/holbertonschool-higher_level_programming/blob/main/python-abc/task_00_abc.py): Démonstration des classes abstraites avec Animal, Dog et Cat. Ce fichier montre comment une classe abstraite sert de modèle et que ses méthodes doivent être implémentées par les classes qui en héritent.

[task_01_duck_typing.py](https://github.com/Mathieu7483/holbertonschool-higher_level_programming/blob/main/python-abc/task_01_duck_typing.py): Illustration du concept de "duck typing" et des interfaces. Les classes Circle et Rectangle adhèrent à l'interface Shape sans vérification explicite de leur type, permettant une grande flexibilité.

[task_02_verboselist.py](https://github.com/Mathieu7483/holbertonschool-higher_level_programming/blob/main/python-abc/task_02_verboselist.py): Exemple d'extension d'une classe native de Python. La classe VerboseList hérite de list et surcharge des méthodes pour ajouter des notifications personnalisées lors des opérations.

[task_03_countediterator.py](https://github.com/Mathieu7483/holbertonschool-higher_level_programming/blob/main/python-abc/task_03_countediterator.py): Un autre exemple d'extension, où la classe CountedIterator étend le comportement d'un itérateur pour suivre le nombre d'itérations effectuées.

[task_04_flyingfish.py](https://github.com/Mathieu7483/holbertonschool-higher_level_programming/blob/main/python-abc/task_04_flyingfish.py): Exploration de l'héritage multiple. Les classes Fish et Bird sont combinées pour créer un FlyingFish, mettant en évidence le comportement de l'ordre de résolution des méthodes (MRO).

[task_05_dragon.py](https://github.com/Mathieu7483/holbertonschool-higher_level_programming/blob/main/python-abc/task_05_dragon.py): Utilisation de "mixins" pour composer le comportement d'une classe. Les classes SwimMixin et FlyMixin fournissent des fonctionnalités modulaires qui sont ensuite intégrées dans la classe Dragon.

# 🛠️ Prérequis

Environnement : Ubuntu 20.04 LTS

Interpréteur : Python 3.8.5

Ligne de code : Chaque fichier Python doit commencer par #!/usr/bin/env python3

# 🚀 Tests

Pour tester chaque tâche, utilisez les scripts main fournis dans le référentiel du projet. Par exemple, pour la tâche 1 :

```Bash

./main_01_duck_typing.py
```

# ✍️ Auteur
[Mathieu GODALIER](https://github.com/Mathieu7483) - Élève en programmation à la Holberton School

# ⚖️ Licence

Ce projet est sous licence MIT. Pour plus de détails, consultez le fichier LICENSE.

# 🙏 Remerciements
Ce projet a été réalisé dans le cadre du cursus de programmation de l'École Holberton. Un grand merci pour l'opportunité de maîtriser ces concepts avancés de la POO en Python.
