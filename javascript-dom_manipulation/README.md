<p align="center"\>
<img src="https://github.com/Mathieu7483/Aiko78-Photgraphy/blob/main/img/Javascript%20image.png"\>
</p\>

-----

# 🚀 0x08. JavaScript - DOM Manipulation

-----

# 📝 Description du Projet

Ce projet a pour objectif d'introduire les fondamentaux du **Développement Web Front-End** en utilisant **JavaScript** pour créer des interfaces utilisateur dynamiques. L'accent est mis sur la manipulation du **DOM (Document Object Model)** pour interagir avec les éléments HTML, la gestion des **événements utilisateur** (clics), et la réalisation de requêtes asynchrones pour intégrer des données externes via la **Fetch API**.

L'ensemble des tâches est conçu pour être exécuté sans rechargement de la page, conformément au principe des applications dynamiques (AJAX).

-----

# 📂 Contenu de l'Exercice

Chaque fichier JavaScript (`X-script.js`) met en œuvre une fonctionnalité spécifique de manipulation du DOM ou de requête réseau.

| Fichier | Objectif Principal | Concepts Clés |
| :--- | :--- | :--- |
| **`0-script.js`** | Changer la couleur du texte de l'en-tête. | `document.querySelector()`, `element.style.color` |
| **`1-script.js`** | Changer la couleur de l'en-tête au clic. | `element.addEventListener('click', ...)` |
| **`2-script.js`** | Ajouter une classe CSS au clic. | `element.classList.add()` |
| **`3-script.js`** | Basculer entre deux classes CSS (`red`/`green`). | `element.classList.toggle()`, Logique conditionnelle |
| **`4-script.js`** | Ajouter un nouvel élément `<li>` à une liste. | `document.createElement()`, `element.appendChild()` |
| **`5-script.js`** | Mettre à jour le contenu textuel de l'en-tête. | `element.textContent` (ou `element.innerHTML`) |
| **`6-script.js`** | Récupérer le nom d'un personnage Star Wars et l'afficher. | **`Fetch API`**, `Promises`, `JSON parsing` |
| **`7-script.js`** | Lister les titres de tous les films Star Wars. | `Fetch API`, Itération sur les résultats, Injection `<li>` |
| **`8-script.js`** | Récupérer une traduction de "Hello" (en français) et l'afficher. | `Fetch API` pour API tierce, Exécution de script dans `<head>` |

-----

# 🛠️ Prérequis

Ce projet est conçu pour une exécution côté client. Aucun environnement de compilation spécifique n'est requis.

  * **Navigateur Web :** Chrome (version 57.0 ou ultérieure).
  * **Standards :** Le code est conforme à la convention **`semistandard`**.

-----

# ⚙️ Compilation et Exécution

Étant des scripts destinés au navigateur, la méthode d'exécution consiste à ouvrir le fichier HTML de test correspondant.

1.  **Cloner le dépôt :**

    ```bash
    git clone https://github.com/holbertonschool-higher_level_programming/javascript-dom_manipulation.git
    cd javascript-dom_manipulation
    ```

2.  **Exécuter un exercice :**
    Ouvrez le fichier HTML de test (`X-main.html`) associé à l'exercice (`X-script.js`) dans votre navigateur web.

    *Exemple pour la tâche 6 :*

    ```bash
    # Ouvrez le fichier dans votre explorateur de fichiers ou utilisez une commande shell appropriée:
    open 6-main.html 
    # ou sous Linux:
    xdg-open 6-main.html
    ```

    Le script `6-script.js` s'exécutera automatiquement, effectuera la requête **Fetch** et mettra à jour le DOM.

-----

# ✍️ **Auteur**

[Mathieu GODALIER](https://github.com/Mathieu7483) - Élève en programmation à la Holberton School

-----

# ⚖️ **Licence**

Ce projet est sous licence MIT. Pour plus de détails, consultez le fichier `LICENSE`.