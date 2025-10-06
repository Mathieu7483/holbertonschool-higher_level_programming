<p align="center">
<img src="https://github.com/Mathieu7483/Aiko78-Photgraphy/blob/main/img/python%20n%C3%A9eon%20carte%20%C3%A9l%C3%A9ctronique.png">
</p>

# 0x0F. RESTful API
# 📝 Description
Ce projet est une exploration complète de l'architecture REST (Representational State Transfer), le standard de facto pour les services web. Il s'agit d'une démarche progressive, allant de la compréhension des protocoles web de base (HTTP/HTTPS) à la consommation d'API via la ligne de commande et Python, pour aboutir au développement et à la sécurisation d'une API simple en utilisant le framework Flask.

# 📚 Concepts Abordés
Protocoles Web : Différences entre HTTP et HTTPS, structure des requêtes/réponses, méthodes et codes de statut.

Consommation d'API : Utilisation de l'outil en ligne de commande curl et de la librairie Python requests pour interagir avec des services externes.

Développement d'API sans framework : Mise en place d'un serveur web basique avec le module standard http.server.

Développement avec Framework : Construction d'une API structurée et routée à l'aide de Flask.

Sécurité des API : Implémentation de mécanismes d'authentification de base (Basic Auth) et par jeton (JWT), incluant la gestion des rôles.

# 📂 Contenu de l'exercice
Ce projet ne contient pas de fichiers à soumettre pour les premières tâches conceptuelles, mais se concentre sur les fichiers Python suivants :

task_02_requests.py : Fonctions Python utilisant la librairie requests pour récupérer et traiter des données JSON depuis une API publique, et convertir le résultat en un fichier CSV.

task_03_http_server.py : Implémentation d'un serveur web basique en Python à l'aide du module standard http.server, capable de répondre à des requêtes GET et de servir des données JSON pour différents endpoints (/data, /status).

task_04_flask.py : Développement d'une API plus complète en utilisant le framework Flask. Ce fichier gère plusieurs routes, des requêtes dynamiques (e.g., /users/<username>) et des requêtes POST pour ajouter de nouvelles données.

task_05_basic_security.py : Intégration de la sécurité dans l'API Flask. Mise en œuvre de l'authentification de base et de l'authentification par jeton JWT (JSON Web Token), incluant une vérification d'accès basée sur les rôles.

# 🛠️ Prérequis
Environnement : Ubuntu 20.04 LTS

Interpréteur : Python 3.8.5

Outils CLI : curl

Librairies Python : requests, Flask, Flask-HTTPAuth, Flask-JWT-Extended, werkzeug.security.

# 🚀 Tests
Les tests de ce projet sont principalement réalisés via la ligne de commande en utilisant curl pour interroger les APIs développées et vérifier les codes de statut HTTP (200 OK, 404 Not Found, 401 Unauthorized, etc.) et le format des données JSON retournées.

# ✍️ Auteur
Mathieu GODALIER - Élève en programmation à la Holberton School

# ⚖️ Licence
Ce projet est sous licence MIT. Pour plus de détails, consultez le fichier LICENSE.
