<p align="center"\>
<img src="https://github.com/Mathieu7483/Aiko78-Photgraphy/blob/main/img/python%20n%C3%A9eon%20carte%20%C3%A9l%C3%A9ctronique.png"\>
</p\>

# 0x11. SQL - Introduction (MySQL)

-----

# 📝 **Description**

Ce projet d'introduction a pour objectif de vous familiariser avec les fondamentaux des **bases de données relationnelles** et du langage **SQL (Structured Query Language)**, en utilisant le SGBD **MySQL**. Les tâches couvrent les concepts de base pour la **définition des données (DDL)**, incluant la création/suppression de bases et de tables, ainsi que la **manipulation des données (DML)**, incluant l'insertion, la sélection, la mise à jour et la suppression d'enregistrements.

-----

# 📚 **Concepts Clés**

  * **Bases de Données Relationnelles** : Comprendre ce qu'est une base de données et pourquoi le modèle relationnel est important.
  * **SQL** : Maîtriser les commandes de base pour interagir avec une base de données.
  * **DDL (Data Definition Language)** : Utilisation des commandes `CREATE` et `DROP` pour structurer la base.
  * **DML (Data Manipulation Language)** : Utilisation des commandes `SELECT`, `INSERT`, `UPDATE` et `DELETE` pour gérer les données.
  * **Clauses Essentielles** : `WHERE`, `ORDER BY`, `LIMIT`, `GROUP BY`.
  * **Fonctions d'Agrégation** : Utilisation de fonctions comme `COUNT()` et `AVG()`.

-----

# 📂 **Contenu de l'exercice**

Chaque fichier est un script SQL conçu pour être exécuté via la ligne de commande (`mysql -u... < file.sql`).

  * [0-list_databases.sql](https://github.com/Mathieu7483/holbertonschool-higher_level_programming/blob/main/SQL_introduction/0-list_databases.sql) : Liste toutes les bases de données sur le serveur MySQL.
  * [1-create_database_if_missing.sql](https://github.com/Mathieu7483/holbertonschool-higher_level_programming/blob/main/SQL_introduction/1-create_database_if_missing.sql) : Crée la base de données `hbtn_0c_0` si elle n'existe pas.
  * [2-remove_database.sql](https://github.com/Mathieu7483/holbertonschool-higher_level_programming/blob/main/SQL_introduction/2-remove_database.sql) : Supprime la base de données `hbtn_0c_0` si elle existe.
  * [3-list_tables.sql](https://github.com/Mathieu7483/holbertonschool-higher_level_programming/blob/main/SQL_introduction/3-list_tables.sql) : Liste toutes les tables d'une base de données spécifiée.
  * [4-first_table.sql](https://github.com/Mathieu7483/holbertonschool-higher_level_programming/blob/main/SQL_introduction/4-first_table.sql) : Crée la table `first_table` avec les colonnes `id` (`INT`) et `name` (`VARCHAR(256)`).
  * [5-full_table.sql](https://github.com/Mathieu7483/holbertonschool-higher_level_programming/blob/main/SQL_introduction/5-full_table.sql) : Affiche la description complète de la table `first_table` sans utiliser les commandes `DESCRIBE` ou `EXPLAIN`.
  * [6-list_values.sql](https://github.com/Mathieu7483/holbertonschool-higher_level_programming/blob/main/SQL_introduction/6-list_values.sql) : Affiche tous les enregistrements (lignes) de la table `first_table`.
  * [7-insert_value.sql](https://github.com/Mathieu7483/holbertonschool-higher_level_programming/blob/main/SQL_introduction/7-insert_value.sql) : Insère un nouvel enregistrement (`id = 89`, `name = 'Best School'`) dans `first_table`.
  * [8-count_89.sql](https://github.com/Mathieu7483/holbertonschool-higher_level_programming/blob/main/SQL_introduction/8-count_89.sql) : Compte le nombre d'enregistrements où `id` est égal à 89 dans la table `first_table`.
  * [9-full_creation.sql](https://github.com/Mathieu7483/holbertonschool-higher_level_programming/blob/main/SQL_introduction/9-full_creation.sql) : Crée la table `second_table` (`id`, `name`, `score`) et insère plusieurs lignes de données initiales.
  * [10-top_score.sql](https://github.com/Mathieu7483/holbertonschool-higher_level_programming/blob/main/SQL_introduction/10-top_score.sql) : Liste tous les enregistrements de `second_table`, classés par score décroissant.
  * [11-best_score.sql](https://github.com/Mathieu7483/holbertonschool-higher_level_programming/blob/main/SQL_introduction/11-best_score.sql) : Liste les enregistrements de `second_table` ayant un score $\ge 10$, classés par score décroissant.
  * [12-no_cheating.sql](https://github.com/Mathieu7483/holbertonschool-higher_level_programming/blob/main/SQL_introduction/12-no_cheating.sql) : Met à jour le score de l'enregistrement dont le `name` est 'Bob' à 10.
  * [13-change_class.sql](https://github.com/Mathieu7483/holbertonschool-higher_level_programming/blob/main/SQL_introduction/13-change_class.sql) : Supprime tous les enregistrements de `second_table` dont le score est $\le 5$.
  * [14-average.sql](https://github.com/Mathieu7483/holbertonschool-higher_level_programming/blob/main/SQL_introduction/14-average.sql) : Calcule la **moyenne** des scores de tous les enregistrements dans `second_table`.
  * [15-groups.sql](https://github.com/Mathieu7483/holbertonschool-higher_level_programming/blob/main/SQL_introduction/15-groups.sql) : Liste le nombre d'enregistrements pour chaque score existant, regroupés et triés par nombre décroissant.
  * [16-no_link.sql](https://github.com/Mathieu7483/holbertonschool-higher_level_programming/blob/main/SQL_introduction/16-no_link.sql) : Liste tous les enregistrements de `second_table` qui ont une valeur définie pour la colonne `name`, triés par score décroissant.


Fichier,Objectif,Concepts Nouveaux
* [100-move_to_utf8.sql](https://github.com/Mathieu7483/holbertonschool-higher_level_programming/blob/main/SQL_introduction/100-move_to_utf8.sql) :"Conversion de la base, d'une table et d'un champ spécifique vers l'encodage utf8mb4 pour la prise en charge complète des caractères Unicode.","ALTER DATABASE, ALTER TABLE, CONVERT TO CHARACTER SET"
* [101-avg_temperatures.sql](https://github.com/Mathieu7483/holbertonschool-higher_level_programming/blob/main/SQL_introduction/101-avg_temperatures.sql) :"Afficher la température moyenne (Fahrenheit) par ville, triée par température décroissante. (Nécessite l'import du dump de données)","GROUP BY, AVG(), ORDER BY"
* [102-top_city.sql](https://github.com/Mathieu7483/holbertonschool-higher_level_programming/blob/main/SQL_introduction/102-top_city.sql) : Afficher le top 3 des villes avec la température moyenne la plus élevée durant les mois de Juillet et Août.,"WHERE (sur mois), GROUP BY, AVG(), LIMIT"
* [103-max_state.sql](https://github.com/Mathieu7483/holbertonschool-higher_level_programming/blob/main/SQL_introduction/103-max_state.sql) : "Afficher la température maximale pour chaque état, ordonnée par nom d'état.","GROUP BY, MAX()"
-----

# 🛠️ **Environnement et Contraintes**

  * **SGBD** : MySQL 8.0
  * **OS** : Ubuntu 22.04 LTS
  * **Règles de Style SQL** :
      * Les mots-clés SQL doivent être en **MAJUSCULES** (`SELECT`, `WHERE`, `CREATE DATABASE`).
      * Chaque fichier SQL doit commencer par un commentaire décrivant la tâche.
      * Une ligne de commentaire doit précéder chaque requête SQL.

-----

# ✍️ **Auteur**

[Mathieu GODALIER](https://github.com/Mathieu7483) - Élève en programmation à la Holberton School

-----

# ⚖️ **Licence**

Ce projet est sous licence MIT. Pour plus de détails, consultez le fichier `LICENSE`.
