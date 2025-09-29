<p align="center">
<img src="https://github.com/Mathieu7483/Aiko78-Photgraphy/blob/main/img/python%20n%C3%A9eon%20carte%20%C3%A9l%C3%A9ctronique.png">
</p>

# 0x0D. Python - Input/Output
# 📝 Description
Ce projet porte sur la maîtrise des opérations d'entrée/sortie (Input/Output) en Python. Les exercices couvrent la manipulation des fichiers texte pour la lecture et l'écriture, et se concentrent particulièrement sur la sérialisation et la désérialisation des structures de données Python en utilisant le format JSON. Ce projet renforce la compréhension de concepts cruciaux tels que l'instruction with (pour la gestion des ressources) et l'accès aux arguments de la ligne de commande.

# 📚 Concepts Abordés
Fichiers (Files) : Lecture (read, readlines), écriture (write), et ajout (append) de contenu.

Gestion des ressources : Utilisation de l'instruction with pour s'assurer que les fichiers sont toujours fermés.

JSON (JavaScript Object Notation) : Sérialisation (conversion d'objets Python en chaîne JSON) et désérialisation (conversion de chaîne JSON en objets Python).

Programmation Orientée Objet (POO) : Ajout de méthodes de sérialisation/désérialisation aux classes d'objets personnalisées.

Algorithmique : Implémentation du triangle de Pascal.

# 📂 Contenu de l'exercice
Fichier	Description
[0-read_file.py]() :	Fonction qui lit un fichier texte (UTF8) et imprime son contenu sur la sortie standard.
[1-write_file.py]()	:Fonction qui écrit une chaîne dans un fichier texte (et écrase le contenu s'il existe).
[2-append_write.py]() :	Fonction qui ajoute une chaîne à la fin d'un fichier texte (et crée le fichier s'il n'existe pas).
[3-to_json_string.py]()	: Fonction qui retourne la représentation JSON (chaîne de caractères) d'un objet Python.
[4-from_json_string.py]()	: Fonction qui retourne un objet (structure de données Python) à partir d'une chaîne JSON.
[5-save_to_json_file.py]()	: Fonction qui écrit un objet Python dans un fichier texte, en utilisant la représentation JSON.
[6-load_from_json_file.py]()	: Fonction qui crée un objet Python à partir d'un "fichier JSON".
[7-add_item.py]()	: Script qui charge des éléments depuis un fichier JSON, ajoute les arguments passés en ligne de commande, et sauvegarde la liste mise à jour.
[8-class_to_json.py]()	: Fonction qui retourne la description dictionnaire d'un objet pour la sérialisation JSON.
[9-student.py]()	: Classe Student avec une méthode to_json pour récupérer sa représentation dictionnaire.
[10-student.py]()	: Classe Student améliorée avec une méthode to_json(attrs=None) permettant de filtrer les attributs à sérialiser.
[11-student.py]()	: Classe Student avec une méthode reload_from_json(json) pour désérialiser et remplacer ses attributs à partir d'un dictionnaire JSON.
[12-pascal_triangle.py]()	: Fonction qui génère le Triangle de Pascal jusqu'à la ligne n.


# 🛠️ Prérequis
Environnement : Ubuntu 20.04 LTS

Interpréteur : Python 3.8.5

Ligne de code : Chaque fichier Python doit commencer par #!/usr/bin/python3

Formatage : Le code doit respecter les règles de pycodestyle (version 2.7.*)

# 🚀 Tests
Les tests de ce projet sont principalement effectués via doctest.

Exécutez les tests pour chaque module avec la commande :

```Bash

python3 -m doctest ./tests/*
```

# ✍️ Auteur
Mathieu GODALIER - Élève en programmation à la Holberton School

# ⚖️ Licence
Ce projet est sous licence MIT. Pour plus de détails, consultez le fichier LICENSE.

# 🙏 Remerciements
Ce projet a été réalisé dans le cadre du cursus de programmation de l'École Holberton. Un grand merci pour l'opportunité d'apprendre et de mettre en pratique ces concepts.
