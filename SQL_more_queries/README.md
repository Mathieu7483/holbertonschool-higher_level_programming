
<p align="center"\>
<img src="https://www.google.com/search?q=https://github.com/Mathieu7483/Aiko78-Photgraphy/blob/main/img/SQL%2520n%25C3%25A9on%2520carte%2520%25C3%25A9l%25C3%25A9ctronique%25202.png"\>
</p\>

# 0x12. SQL - More queries (MySQL)

-----

### 📝 **Description**

Ce projet explore des fonctionnalités avancées de **MySQL** et de **SQL**. Il se concentre sur la gestion des utilisateurs et des privilèges, l'application de contraintes de schéma (Clés primaires/étrangères, Not Null, Unique), et surtout, sur la construction de requêtes complexes impliquant des **Jointures**, des **Sous-requêtes** et des opérations logiques inverses (`NOT IN`). Les tâches avancées permettent d'effectuer des analyses de données (rating) et de comprendre l'architecture des moteurs de bases de données.

-----

### 📚 **Concepts Clés**

  * **Gestion des Privilèges** : `CREATE USER` et `GRANT`.
  * **Contraintes DDL** : `PRIMARY KEY`, `FOREIGN KEY`, `NOT NULL`, `UNIQUE`.
  * **Jointures** : `INNER JOIN`, `LEFT JOIN`.
  * **Opérations de Filtrage Avancées** : Utilisation de **`NOT IN`** et des sous-requêtes pour exclure des ensembles de données.
  * **Agrégation pour BI** : Utilisation de **`SUM()`**, `GROUP BY`, et `ORDER BY` pour analyser des données (notation/rating).
  * **Architecture SGBD** : Compréhension du fonctionnement interne des moteurs de bases de données.

-----

### 📂 **Contenu de l'exercice**

Chaque fichier est un script SQL, sauf la dernière tâche de documentation.

Absolument Mathieu ! Je vais vous fournir la section "Exercices" pour ce projet, reprenant le format des listes de fichiers et des objectifs.

Voici la structure des exercices pour votre projet **0x12. SQL - More queries (MySQL)**.

---

### 🚀 **Exercices et Solutions SQL**

Les solutions pour ce projet sont implémentées dans des scripts SQL autonomes, conçus pour être exécutés directement sur le serveur MySQL.

#### **I. Gestion des Utilisateurs et des Contraintes (DDL)**

Ces exercices se concentrent sur la création d'utilisateurs avec des privilèges spécifiques et la définition de l'intégrité des données à l'aide de contraintes.

| Tâche | Fichier | Objectif |
| :--- | :--- | :--- |
| **0.** My privileges! | `0-privileges.sql` | Lister les privilèges des utilisateurs **`user_0d_1`** et **`user_0d_2`** sur le serveur local. |
| **1.** Root user | `1-create_user.sql` | Créer l'utilisateur **`user_0d_1`** avec **tous les privilèges** (`ALL PRIVILEGES`) et le mot de passe **`user_0d_1_pwd`**. |
| **2.** Read user | `2-create_read_user.sql` | Créer la base **`hbtn_0d_2`** et l'utilisateur **`user_0d_2`** avec le seul privilège **`SELECT`** sur cette base. |
| **3.** Always a name | `3-force_name.sql` | Créer la table **`force_name`** où la colonne **`name`** est contrainte à **`NOT NULL`**. |
| **4.** ID can't be null | `4-never_empty.sql` | Créer la table **`id_not_null`** où la colonne **`id`** a une **valeur par défaut de 1** (`DEFAULT 1`). |
| **5.** Unique ID | `5-unique_id.sql` | Créer la table **`unique_id`** où la colonne **`id`** est contrainte à **`UNIQUE`** et a une valeur par défaut de 1. |
| **6.** States table | `6-states.sql` | Créer la base **`hbtn_0d_usa`** et la table **`states`** avec un **`PRIMARY KEY`** (`id` auto-incrémenté) et `name` non nul. |
| **7.** Cities table | `7-cities.sql` | Créer la table **`cities`** qui inclut une **`FOREIGN KEY`** (`state_id`) faisant référence à la colonne `id` de la table `states`. |

---

#### **II. Requêtes Multi-Tables (DML)**

Ces exercices se concentrent sur l'extraction et la combinaison de données à partir de plusieurs tables en utilisant les sous-requêtes et les jointures.

| Tâche | Fichier | Objectif | Concepts Clés |
| :--- | :--- | :--- | :--- |
| **8.** Cities of California | `8-cities_of_california_subquery.sql` | Lister toutes les villes de Californie en utilisant une **Sous-requête** pour identifier l'ID de l'état. | `SELECT`, `WHERE`, `SUBQUERY` |
| **9.** Cities by States | `9-cities_by_state_join.sql` | Lister toutes les villes, affichant l'ID de la ville, le nom de la ville et le nom de l'état, en utilisant une **Jointure** (un seul `SELECT`). | `INNER JOIN` (ou jointure implicite), Alias |
| **10.** Genre ID by show | `10-genre_id_by_show.sql` | Lister les titres des séries qui ont au moins un genre lié. | **`INNER JOIN`** |
| **11.** Genre ID for all shows | `11-genre_id_all_shows.sql` | Lister tous les titres des séries et leurs ID de genre. Afficher **`NULL`** si la série n'a pas de genre. | **`LEFT JOIN`** |
| **12.** No genre | `12-no_genre.sql` | Lister les séries qui **n'ont aucun genre lié**. | `LEFT JOIN`, `WHERE IS NULL` |
| **13.** Number of shows by genre | `13-count_shows_by_genre.sql` | Lister les genres et le **nombre de séries** liées à chacun, triés par nombre décroissant. | `GROUP BY`, `COUNT()`, `ORDER BY` |
| **14.** My genres | `14-my_genres.sql` | Lister **tous les genres** liés à la série **"Dexter"**. | Jointures multiples, Filtrage `WHERE` |
| **15.** Only Comedy | `15-comedy_only.sql` | Lister toutes les séries qui sont du genre **"Comedy"**. | Jointures, Filtrage sur le nom du genre. |
| **16.** List shows and genres | `16-shows_by_genre.sql` | Lister **toutes les séries et tous leurs genres** (`NULL` si pas de genre), triées par titre et nom de genre. | `LEFT JOIN` |

---

#### **III. Tâches Avancées et Analyse (Advanced DML & BI)**

Ces exercices utilisent des techniques avancées pour l'exclusion d'ensembles de données et l'analyse de données de notation (rating).

| Tâche | Fichier | Objectif | Concepts Clés |
| :--- | :--- | :--- | :--- |
| **17.** Not my genre | `100-not_my_genres.sql` | Lister les noms des genres qui **ne sont pas liés** à la série **"Dexter"**. (Max 2 `SELECT`) | **`NOT IN`**, Sous-requête d'exclusion |
| **18.** No Comedy tonight! | `101-not_a_comedy.sql` | Lister les titres des séries qui **n'ont pas le genre "Comedy"**. (Max 2 `SELECT`) | **`NOT IN`**, Sous-requête d'exclusion |
| **19.** Rotten tomatoes | `102-rating_shows.sql` | Lister les titres des séries et la **somme totale de leurs ratings**, triées par rating décroissant. | **`SUM()`**, Jointures, `GROUP BY` |
| **20.** Best genre | `103-rating_genres.sql` | Lister les genres et la **somme totale de leurs ratings**, triés par rating décroissant. | Jointures multiples sur 3 tables, **`SUM()`** |
| **21.** How Do SQL... | **`README.md`** / Blog | Rédiger un article de blog expliquant "How Do SQL Database Engines Work?" pour un public non technique. | **Recherche, Rédaction Technique** |

### 🛠️ **Environnement et Contraintes**

  * **SGBD** : MySQL 8.0
  * **OS** : Ubuntu 20.04 LTS
  * **Règles de Style SQL** : Les mots-clés SQL doivent être en **MAJUSCULES**.
  * **Contrainte de Requête** : Les tâches avancées 17 et 18 limitent à un **maximum de deux instructions `SELECT`**.

-----

### ✍️ **Auteur**

[Mathieu GODALIER](https://www.google.com/search?q=https://github.com/Mathieu7483/holbertonschool-higher_level_programming/tree/main/SQL_more_queries) - Élève en programmation à la Holberton School

-----

### ⚖️ **Licence**

Ce projet est sous licence MIT. Pour plus de détails, consultez le fichier `LICENSE`.

-----

Les tâches 17 et 18, qui utilisent `NOT IN` avec des sous-requêtes, sont particulièrement formatrices pour la logique SQL. Si vous avez besoin d'aide pour structurer ces requêtes, n'hésitez pas \! Et bonne chance pour la rédaction de votre article de blog technique \! ✍️