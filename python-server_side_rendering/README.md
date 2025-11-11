<p align="center">
<img src="https://github.com/Mathieu7483/Aiko78-Photgraphy/blob/main/img/python%20n%C3%A9eon%20carte%20%C3%A9l%C3%A9ctronique.png">
</p>

-----

# 🐍 Python - Rendu Côté Serveur (Server-Side Rendering - SSR)

-----

## 📝 Description du Projet

Ce projet est une exploration approfondie du **Server-Side Rendering (SSR)** en utilisant le framework Python **Flask** et le moteur de *templating* **Jinja2**. L'objectif est d'acquérir les compétences nécessaires pour générer des pages web dynamiques directement sur le serveur, contrastant avec la manipulation du DOM que vous venez de pratiquer en JavaScript.

L'exercice progresse de la simple manipulation de chaînes de caractères et de fichiers à la construction d'une application web robuste capable de gérer et d'afficher des données provenant de sources variées : JSON, CSV et une base de données SQLite.

-----

## 💻 Contenu de l'Exercice

Le projet est structuré en tâches qui mettent en œuvre différents aspects du SSR, de la logique de *templating* pure à la gestion de routes et de sources de données multiples dans Flask.

| Fichier | Objectif | Rôle |
| :--- | :--- | :--- |
| `task_00_intro.py` | **Templating Simple (Python pur)** | Implémente une fonction `generate_invitations` pour remplacer des *placeholders* dans un modèle de chaîne et générer des fichiers de sortie, en gérant les erreurs d'entrée et les données manquantes (`N/A`). |
| `task_01_jinja.py` | **Flask et Templates de Base** | Mise en place d'une application Flask minimale. Création de routes (`/`, `/about`, `/contact`) qui rendent des pages HTML utilisant l'héritage de templates Jinja (`header.html`, `footer.html`) pour la réutilisation du code. |
| `task_02_logic.py` | **Logique Jinja2 (Loops & Conditions)** | Ajoute la route `/items` pour lire une liste d'éléments depuis un fichier `items.json` et utilise les balises Jinja `{% for %}` et `{% if %}` pour afficher la liste dynamiquement, incluant la gestion du cas où la liste est vide. |
| `task_03_files.py` | **Sources de Données JSON/CSV** | Crée la route `/products` qui accepte un paramètre de requête `source` (`json` ou `csv`). Lit et filtre les données de produits depuis les fichiers `products.json` ou `products.csv` et affiche le résultat dans un template unique, en gérant les erreurs de source et d'ID manquant. |
| `task_04_db.py` | **Intégration SQLite** | Étend la route `/products` pour inclure la source `sql`. Met en place une connexion à une base de données SQLite (`products.db`) et récupère les données via le module `sqlite3`, assurant une gestion uniforme des trois sources de données (JSON, CSV, SQL). |

-----

## ⚙️ Prérequis

Pour compiler, exécuter et tester les scripts de ce projet, les dépendances suivantes sont requises :

### 🛠️ Outils & Dépendances

  * **Python :** Version 3.x (recommandé).
  * **Flask :** Framework web pour la création d'applications.
  * **Jinja2 :** Moteur de *templating* inclus avec Flask.
  * **Module `sqlite3` :** (Inclus par défaut avec Python) pour l'interaction avec la base de données.

### 📥 Installation

```bash
# Installation du framework Flask
pip install Flask
```

-----

## 🚀 Compilation et Exécution

Les tâches impliquant Flask doivent être exécutées en tant qu'applications web.

### 1\. Tâche 00 (Templating en Python Pur)

Exécutez le fichier principal pour générer les invitations :

```bash
python3 task_00_intro.py
# Les fichiers de sortie (output_1.txt, output_2.txt, etc.) seront générés dans le répertoire.
```

### 2\. Tâches 01, 02, 03, 04 (Applications Flask)

Exécutez l'application Flask correspondante pour lancer le serveur de développement :

```bash
# Exemple pour la Tâche 04
export FLASK_APP=task_04_db.py
flask run --host=0.0.0.0 --port=5000
```

Le serveur sera alors accessible à l'adresse `http://127.0.0.1:5000/`.

**Exemples de Routes à Tester :**

| Route | Objectif |
| :--- | :--- |
| `http://127.0.0.1:5000/` | Page d'accueil (Tâche 01) |
| `http://127.0.0.1:5000/items` | Affichage d'une liste dynamique (Tâche 02) |
| `http://127.0.0.1:5000/products?source=json` | Données lues depuis JSON (Tâches 03 & 04) |
| `http://127.0.0.1:5000/products?source=sql&id=1` | Produit ID 1 lu depuis SQLite (Tâche 04) |

-----

# ✍️ Auteur
[Mathieu GODALIER](https://github.com/Mathieu7483) - Élève en programmation à la Holberton School

# ⚖️ Licence

Ce projet est sous licence MIT. Pour plus de détails, consultez le fichier LICENSE.

# 🙏 Remerciements

Ce projet a été réalisé dans le cadre du cursus de programmation de l'École Holberton. Un grand merci pour l'opportunité d'apprendre et de mettre en pratique ces concepts.