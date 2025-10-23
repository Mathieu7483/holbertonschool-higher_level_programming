<p align="center"\>
<img src="https://github.com/Mathieu7483/Aiko78-Photgraphy/blob/main/img/python%20n%C3%A9eon%20carte%20%C3%A9l%C3%A9ctronique.png"\>
</p\>

# 0x13. Python - Object-relational mapping (ORM)

-----

# 📝 **Description**

Ce projet marque la transition entre l'écriture manuelle de requêtes **SQL** et l'utilisation de l'approche **Object-Oriented Programming (OOP)** pour interagir avec les bases de données.

Nous explorerons deux méthodes :

1.  **Connexion directe avec `MySQLdb`** : Pour comprendre l'exécution des requêtes SQL depuis un script Python. Cela inclut l'apprentissage des bonnes pratiques de sécurité contre l'**Injection SQL**.
2.  **Mapping Objet-Relationnel (ORM) avec `SQLAlchemy`** : Pour manipuler les données de la base en utilisant uniquement des **objets Python**. L'ORM permet de s'affranchir de l'écriture SQL, rendant le code plus portable, lisible et fortement lié à la logique métier.

-----

# 📚 **Concepts Clés**

  * **Interconnexion Python/MySQL** : Comment le module `MySQLdb` permet d'établir une connexion et d'exécuter des commandes.
  * **Sécurité des Données** : Prévention des failles de sécurité courantes comme l'**Injection SQL** en utilisant la paramétrisation des requêtes.
  * **Object-Relational Mapping (ORM)** : Le principe de faire correspondre les classes et les objets Python aux tables et aux lignes de la base de données.
  * **`SQLAlchemy`** : Maîtrise de cet ORM pour :
      * **Définir le Modèle** : Mapper une classe Python (ex: `State`) à une table MySQL (`states`).
      * **Créer une Session** : Utiliser la session pour interagir avec la base.
      * **Opérations CRUD** : Sélectionner (`query`), insérer (`add`), mettre à jour (`update`), et supprimer (`delete`) des objets.

-----

# 🗂️ **Fichiers de Modèle**

Les fichiers de modèles définissent la structure de la base de données en termes de classes Python, une étape fondamentale de l'ORM.

| Fichier | Description | Concepts Clés |
| :--- | :--- | :--- |
| **[model_state.py](https://github.com/Mathieu7483/holbertonschool-higher_level_programming/blob/main/python-object_relational_mapping/model_state.py)** | Définition de la classe **`State`** et de l'instance **`Base`** de SQLAlchemy. `State` est mappée à la table MySQL `states` avec les colonnes `id` (clé primaire) et `name`. | `declarative_base()`, `Column`, `Integer`, `String`, `PrimaryKeyConstraint` |
| **[model_city.py](https://github.com/Mathieu7483/holbertonschool-higher_level_programming/blob/main/python-object_relational_mapping/model_city.py)** | Définition de la classe **`City`**. Mappée à la table `cities` et incluant une **clé étrangère** (`state_id`) vers la table `states`. | `ForeignKey`, `relationship` (implicite ou explicite) |

-----

# 💻 **Exercices**

Ce projet est divisé en deux phases majeures : **MySQLdb** pour la connexion de bas niveau (tâches 0 à 5), puis **SQLAlchemy** pour l'abstraction ORM (tâches 6 à 14).

#### **Phase 1 : Utilisation de `MySQLdb` (Connexion Directe)**

Scripts exécutant des requêtes SQL via le module `MySQLdb`.

| Fichier | Objectif | Note Clé |
| :--- | :--- | :--- |
| **[0-select_states.py](https://github.com/Mathieu7483/holbertonschool-higher_level_programming/blob/main/python-object_relational_mapping/0-select_states.py)** | Lister tous les états. | Utilisation simple de `MySQLdb.connect()` et `cursor.execute()`. |
| **[1-filter_states.py](https://github.com/Mathieu7483/holbertonschool-higher_level_programming/blob/main/python-object_relational_mapping/1-filter_states.py)** | Filtrer les états dont le nom commence par 'N'. | Utilisation de la clause SQL `WHERE name LIKE 'N%'`. |
| **[2-my_filter_states.py](https://github.com/Mathieu7483/holbertonschool-higher_level_programming/blob/main/python-object_relational_mapping/2-my_filter_states.py)** | Filtrer les états par un nom fourni en argument. | **Vulnérabilité à l'Injection SQL** : Utilisation de `str.format()` pour construire la requête. |
| **[3-my_safe_filter_states.py](https://github.com/Mathieu7483/holbertonschool-higher_level_programming/blob/main/python-object_relational_mapping/3-my_safe_filter_states.py)** | Filtrer les états par un nom fourni, mais de manière **sécurisée**. | **Paramétrisation des requêtes** (`cursor.execute(sql, (arg,))`) pour se protéger contre l'**Injection SQL**. |
| **[4-cities_by_state.py](https://github.com/Mathieu7483/holbertonschool-higher_level_programming/blob/main/python-object_relational_mapping/4-cities_by_state.py)** | Lister toutes les villes avec le nom de leur état. | Utilisation d'une **Jointure** SQL (une seule `execute()`). |
| **[5-filter_cities.py](https://github.com/Mathieu7483/holbertonschool-higher_level_programming/blob/main/python-object_relational_mapping/5-filter_cities.py)** | Lister les villes d'un état spécifique (nom fourni en argument). | Utilisation d'une **Jointure** et de la **Sécurité contre l'Injection SQL**. |


### Fichiers SQL de Base de Données

| Nom du Fichier | Description | Liens Rapides |
| :------------- | :---------- | :------------ |
| `0-select_states.sql` | Script SQL pour sélectionner toutes les entrées de la table `states`. | [Voir sur GitHub](https://github.com/Mathieu7483/holbertonschool-higher_level_programming/blob/main/python-object_relational_mapping/0-select_states.sql) |
| `4-cities_by_states.sql` | Script SQL pour lister toutes les villes (`cities`) avec leur État (`state`) associé, en utilisant une jointure (probablement pour la création de la vue ou une requête de sélection). | [Voir sur GitHub](https://github.com/Mathieu7483/holbertonschool-higher_level_programming/blob/main/python-object_relational_mapping/4-cities_by_state.sql) |
-----

#### **Phase 2 : Utilisation de `SQLAlchemy` (ORM)**

Scripts utilisant les modèles Python définis dans `model_state.py` et `model_city.py` pour interagir avec la base sans écrire de SQL.

| Fichier | Objectif | Fonctionnalité ORM |
| :--- | :--- | :--- |
| **[6-model_state.py](https://github.com/Mathieu7483/holbertonschool-higher_level_programming/blob/main/python-object_relational_mapping/model_state.py)** | Initialisation de la base de données et création de la table `states` via le modèle. | `Base.metadata.create_all(engine)` |
| **[7-model_state_fetch_all.py](https://github.com/Mathieu7483/holbertonschool-higher_level_programming/blob/main/python-object_relational_mapping/7-model_state_fetch_all.py)** | Lister tous les objets `State`. | `session.query(State).order_by(State.id).all()` |
| **[8-model_state_fetch_first.py](https://github.com/Mathieu7483/holbertonschool-higher_level_programming/blob/main/python-object_relational_mapping/8-model_state_fetch_first.py)** | Afficher le premier objet `State` par ID. | `session.query(State).order_by(State.id).first()` |
| **[9-model_state_filter_a.py](https://github.com/Mathieu7483/holbertonschool-higher_level_programming/blob/main/python-object_relational_mapping/9-model_state_filter_a.py)** | Lister les états dont le nom contient la lettre 'a'. | `session.query(State).filter(State.name.like('%a%'))` |
| **[10-model_state_my_get.py](https://github.com/Mathieu7483/holbertonschool-higher_level_programming/blob/main/python-object_relational_mapping/10-model_state_my_get.py)** | Récupérer un état par son nom. | `session.query(State).filter(State.name == nom).one_or_none()` |
| **[11-model_state_insert.py](https://github.com/Mathieu7483/holbertonschool-higher_level_programming/blob/main/python-object_relational_mapping/11-model_state_insert.py)** | Ajouter un nouvel état ("Louisiana"). | Création d'un objet Python (`State(...)`), `session.add()`, `session.commit()`. |
| **[12-model_state_update_id_2.py](https://github.com/Mathieu7483/holbertonschool-higher_level_programming/blob/main/python-object_relational_mapping/12-model_state_update_id_2.py)**| Mettre à jour le nom de l'état avec `id=2` à "New Mexico". | Récupération de l'objet, modification de l'attribut (`state.name = '...'`), `session.commit()`. |
| **[13-model_state_delete_a.py](https://github.com/Mathieu7483/holbertonschool-higher_level_programming/blob/main/python-object_relational_mapping/13-model_state_delete_a.py)** | Supprimer les états dont le nom contient 'a'. | `session.query(State).filter(...).delete()`, `session.commit()`. |
| **[14-model_city_fetch_by_state.py](https://github.com/Mathieu7483/holbertonschool-higher_level_programming/blob/main/python-object_relational_mapping/14-model_city_fetch_by_state.py)**| Lister toutes les villes avec le nom de leur état. | Jointure implicite (`session.query(State, City).filter(State.id == City.state_id)`) |

### Fichiers de Modèles et Requêtes SQL

| Nom du Fichier | Description | Liens Rapides |
| :------------- | :---------- | :------------ |
| `6-model_state.sql` | Définit la **classe `State`** pour l'ORM (probablement SQLAlchemy), mappée à la table `states` de la base de données. | [Voir sur GitHub](https://github.com/Mathieu7483/holbertonschool-higher_level_programming/blob/main/python-object_relational_mapping/6-model_state.sql) |
| `7-model_state_fetch_all.sql` | Script Python qui se connecte à la base de données et utilise le **modèle `State`** pour récupérer **toutes** les entrées de la table `states`. | [Voir sur GitHub](https://github.com/Mathieu7483/holbertonschool-higher_level_programming/blob/main/python-object_relational_mapping/7-model_state_fetch_all.sql) |
| `14-model_city_fetch_by_state.sql` | Script Python qui joint les **modèles `City` et `State`** pour lister toutes les villes et leur état correspondant, illustrant une relation **One-to-Many** dans l'ORM. | [Voir sur GitHub](https://github.com/Mathieu7483/holbertonschool-higher_level_programming/blob/main/python-object_relational_mapping/14-model_city_fetch_by_state.sql) |


-----

# 🛠️ **Installation et Configuration**

Ce projet nécessite l'installation des modules suivants dans votre environnement Python :

1.  **MySQL Server** (version 8.0+)
2.  **`mysqlclient`** (ou `MySQLdb`) : Version **2.0.x**
    ```bash
    $ sudo apt-get install python3-dev libmysqlclient-dev zlib1g-dev
    $ sudo pip3 install mysqlclient==2.0.3
    ```
3.  **`SQLAlchemy`** : Version **1.4.x**
    ```bash
    $ sudo pip3 install SQLAlchemy==1.4.22
    ```

-----

# ✍️ **Auteur**

[Mathieu GODALIER](https://www.google.com/search?q=https://github.com/Mathieu7483/holbertonschool-higher_level_programming/tree/main/SQL_more_queries) - Élève en programmation à la Holberton School

-----

# ⚖️ **Licence**

Ce projet est sous licence MIT. Pour plus de détails, consultez le fichier `LICENSE`.

