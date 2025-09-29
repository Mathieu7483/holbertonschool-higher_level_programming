<p align="center">
<img src="https://github.com/Mathieu7483/Aiko78-Photgraphy/blob/main/img/python%20n%C3%A9eon%20carte%20%C3%A9l%C3%A9ctronique.png">
</p>

# 0x0E. Python - Serialization
# 📝 Description
Ce projet explore la sérialisation et le marshaling, des mécanismes essentiels pour la persistance et la transmission des données. Il couvre la transformation d'objets en formats stockables ou transmissibles (JSON, Pickle, XML) et leur reconstitution (désérialisation). La progression des tâches vous permet de manipuler différents formats et d'appliquer la sérialisation à des structures de données simples (dictionnaires) ainsi qu'à des objets de classes personnalisées.

# 📚 Concepts Abordés
Sérialisation & Désérialisation : Conversion d'objets Python en un format de données (et inversement).

JSON : Utilisation du module json pour sérialiser des dictionnaires et des listes.

Pickle : Utilisation du module pickle pour sérialiser et désérialiser des instances de classes personnalisées.

Interfaçage de Formats : Conversion de données d'un format à l'autre (CSV vers JSON).

# XML : Exploration de la sérialisation et désérialisation en XML en utilisant xml.etree.ElementTree.

# 📂 Contenu de l'exercice
[task_00_basic_serialization.py]()	Implémente la sérialisation et désérialisation de base d'un dictionnaire Python vers/depuis un fichier JSON.
[task_01_pickle.py]()	Définit la classe CustomObject avec des méthodes de sérialisation et désérialisation basées sur le module pickle, démontrant la gestion des objets personnalisés.
[task_02_csv.py]()	Contient la fonction convert_csv_to_json qui lit des données depuis un fichier CSV et les convertit en un fichier JSON, en utilisant les modules csv et json.
[task_03_xml.py]()	Implémente les fonctions serialize_to_xml et deserialize_from_xml pour convertir un dictionnaire Python vers/depuis le format XML en utilisant xml.etree.ElementTree.


# 🛠️ Prérequis
Environnement : Ubuntu 20.04 LTS

Interpréteur : Python 3.8.5

Modules : json, pickle, csv, xml.etree.ElementTree.

# 🚀 Tests
Les tests de ce projet sont manuels et visent à vérifier la création et l'intégrité des fichiers de données intermédiaires (data.json, object.pkl, data.xml).

Exemple de vérification pour la Tâche 0 :

Exécuter le script de test.

Vérifier que le fichier data.json est créé et contient la représentation JSON correcte du dictionnaire.

Vérifier que la fonction de désérialisation recrée le dictionnaire Python original.

# ✍️ Auteur
[Mathieu GODALIER](https://github.com/Mathieu7483) - Élève en programmation à la Holberton School

# ⚖️ Licence

Ce projet est sous licence MIT. Pour plus de détails, consultez le fichier LICENSE.

# 🙏 Remerciements

Ce projet a été réalisé dans le cadre du cursus de programmation de l'École Holberton. Un grand merci pour l'opportunité d'apprendre et de mettre en pratique ces concepts.