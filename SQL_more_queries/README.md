<p align="center">
<img src=https://github.com/Mathieu7483/Aiko78-Photgraphy/blob/main/img/python%20n%C3%A9eon%20carte%20%C3%A9l%C3%A9ctronique.png>
</p>

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

#### **Tâches Mandatoires (0 à 16)**

  * **Gestion des Users & Privilèges** : `0-privileges.sql`, `1-create_user.sql`, `2-create_read_user.sql`.
  * **Contraintes DDL** : `3-force_name.sql`, `4-never_empty.sql`, `5-unique_id.sql`, `6-states.sql`, `7-cities.sql`.
  * **Requêtes Multi-Tables** :
      * **Sous-requêtes** : `8-cities_of_california_subquery.sql`.
      * **Jointures** : `9-cities_by_state_join.sql`, `10-genre_id_by_show.sql`, `11-genre_id_all_shows.sql`, `12-no_genre.sql`, `13-count_shows_by_genre.sql`, `14-my_genres.sql`, `15-comedy_only.sql`, `16-shows_by_genre.sql`.

#### **Tâches Avancées (17 à 21)**

| Fichier | Objectif | Concepts Nouveaux |
| :--- | :--- | :--- |
| `100-not_my_genres.sql` | Liste tous les genres qui **ne sont pas liés** à la série **"Dexter"**. | Requête combinant **`NOT IN`** et **Sous-requête** pour l'exclusion d'ensembles. |
| `101-not_a_comedy.sql` | Liste toutes les séries qui **n'appartiennent pas** au genre **"Comedy"**. | Application du pattern `NOT IN` pour exclure les séries ayant un genre spécifique. |
| `102-rating_shows.sql` | Liste les séries et la **somme totale de leurs ratings**, triées par rating décroissant. | `SUM()`, Jointures multiples, `GROUP BY` pour l'agrégation de données de notation. |
| `103-rating_genres.sql` | Liste les genres et la **somme totale de leurs ratings**, triés par rating décroissant. | Agrégation de `SUM()` à travers trois tables liées (`tv_genres`, `tv_show_genres`, `tv_show_ratings`). |
| **Blog Post (Non-SQL)** | Rédaction d'un article de blog expliquant "How Do SQL Database Engines Work?" pour un public non technique, incluant des diagrammes et des exemples. | **Recherche et Vulgarisation Technique.** |

-----

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
