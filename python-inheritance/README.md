<p align="center">
<img src="https://github.com/Mathieu7483/Aiko78-Photgraphy/blob/main/img/python%20n%C3%A9eon%20carte%20%C3%A9l%C3%A9ctronique.png">
</p>

# 0x0A. Python - Inheritance
# 📝 Description

Ce projet se concentre sur le concept d'héritage en Python. Il explore comment créer de nouvelles classes à partir de classes existantes, en réutilisant le code et en ajoutant des fonctionnalités spécifiques. Les exercices couvrent la recherche d'attributs et de méthodes, la vérification du type d'objet, la validation des données dans les classes parentes, et l'implémentation de classes enfants qui héritent et étendent les fonctionnalités de leurs parents, comme des formes géométriques.

# 📂 Contenu de l'exercice

Ce répertoire contient les fichiers source des classes, chacun illustrant un concept clé de l'héritage.

[0-lookup.py](https://github.com/Mathieu7483/holbertonschool-higher_level_programming/blob/main/python-inheritance/0-lookup.py): Une fonction qui retourne la liste des attributs et méthodes d'un objet en utilisant la fonction dir().

[1-my_list.py](https://github.com/Mathieu7483/holbertonschool-higher_level_programming/blob/main/python-inheritance/1-my_list.py): Une classe MyList qui hérite de la classe list et ajoute une méthode pour imprimer la liste triée.

[2-is_same_class.py](https://github.com/Mathieu7483/holbertonschool-higher_level_programming/blob/main/python-inheritance/2-is_same_class.py): Une fonction qui vérifie si un objet est exactement une instance d'une classe donnée.

[3-is_kind_of_class.py](https://github.com/Mathieu7483/holbertonschool-higher_level_programming/blob/main/python-inheritance/3-is_kind_of_class.py): Une fonction qui vérifie si un objet est une instance de la classe ou d'une de ses classes parentes.

[4-inherits_from.py](https://github.com/Mathieu7483/holbertonschool-higher_level_programming/blob/main/python-inheritance/4-inherits_from.py): Une fonction qui vérifie si un objet est une instance d'une classe qui a hérité d'une autre classe.

[5-base_geometry.py](https://github.com/Mathieu7483/holbertonschool-higher_level_programming/blob/main/python-inheritance/5-base_geometry.py): Une classe de base vide pour des formes géométriques.

[6-base_geometry.py](https://github.com/Mathieu7483/holbertonschool-higher_level_programming/blob/main/python-inheritance/6-base_geometry.py): Ajout d'une méthode area() qui lève une exception pour indiquer qu'elle doit être implémentée par les classes enfants.

[7-base_geometry.py](https://github.com/Mathieu7483/holbertonschool-higher_level_programming/blob/main/python-inheritance/7-base_geometry.py): Ajout d'une méthode integer_validator() pour valider que les attributs sont des entiers positifs.

[8-rectangle.py](https://github.com/Mathieu7483/holbertonschool-higher_level_programming/blob/main/python-inheritance/8-rectangle.py): Création d'une classe Rectangle qui hérite de BaseGeometry et utilise la méthode de validation.

[9-rectangle.py](https://github.com/Mathieu7483/holbertonschool-higher_level_programming/blob/main/python-inheritance/9-rectangle.py): Complément de la classe Rectangle avec une implémentation de la méthode area() et une représentation sous forme de chaîne de caractères.

[10-square.py](https://github.com/Mathieu7483/holbertonschool-higher_level_programming/blob/main/python-inheritance/10-square.py): Création d'une classe Square qui hérite de Rectangle.

[11-square.py](https://github.com/Mathieu7483/holbertonschool-higher_level_programming/blob/main/python-inheritance/11-square.py): Amélioration de la classe Square avec une représentation spécifique sous forme de chaîne de caractères.

[100-my_int.py](https://github.com/Mathieu7483/holbertonschool-higher_level_programming/blob/main/python-inheritance/100-my_int.py): Une classe MyInt qui hérite de la classe int. Cette classe surpasse le comportement par défaut des opérateurs == et != en les inversant, montrant comment le polymorphisme peut être utilisé pour modifier le comportement de base.

[101-add_attribute.py](https://github.com/Mathieu7483/holbertonschool-higher_level_programming/blob/main/python-inheritance/101-add_attribute.py): Une fonction qui ajoute un nouvel attribut à un objet. Elle gère les exceptions en vérifiant la capacité de l'objet à accepter de nouveaux attributs, ce qui est un bon exemple de gestion des erreurs et de l'inspection dynamique des objets en Python.

# 🛠️ Prérequis

Environnement : Ubuntu 20.04 LTS

Interpréteur : Python 3.8.5

Ligne de code : Chaque fichier Python doit commencer par #!/usr/bin/python3

Formatage : Le code doit respecter les règles de pycodestyle (version 2.7.*)

# 🚀 Tests

Pour tester les fichiers, vous pouvez utiliser les scripts main fournis. Par exemple, pour la tâche 11 :

```Bash

./11-main.py
```

# ✍️ Auteur
[Mathieu GODALIER](https://github.com/Mathieu7483) - Élève en programmation à la Holberton School

# ⚖️ Licence

Ce projet est sous licence MIT. Pour plus de détails, consultez le fichier LICENSE.

# 🙏 Remerciements

Ce projet a été réalisé dans le cadre du cursus de programmation de l'École Holberton. Un grand merci pour l'opportunité d'apprendre et de mettre en pratique ces concepts.
