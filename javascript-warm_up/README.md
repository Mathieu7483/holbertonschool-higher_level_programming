<p align="center"\>
<img src="https://github.com/Mathieu7483/Aiko78-Photgraphy/blob/main/img/Javascript%20image.png"\>
</p\>

# 0x07. JavaScript - Warm Up (Node.js Scripting)

-----

# 📝 **Description du Projet**

Ce projet constitue une initiation intensive aux concepts fondamentaux de la programmation en **JavaScript (JS)**. L'objectif est de maîtriser les éléments de base du langage — variables, types de données, opérateurs, structures de contrôle, fonctions, et manipulation des arguments — en exécutant les scripts côté serveur via **Node.js**.

Cette étape est un préambule indispensable avant d'attaquer la dynamique du front-end et des API (comme vous l'avez fait en Python), en vue de rendre interactif le projet HBnB.

# 🎯 **Objectifs d'Apprentissage et Compétences Acquises**

Vous devez désormais non seulement coder en JS, mais aussi **justifier** les choix de déclaration de variables et la structure de vos fonctions.

## **I. Fondations du Langage**

  * **Exécution de Script** : Savoir configurer et exécuter un fichier JS *via* **Node.js** (`#!/usr/bin/node`).
  * **Déclaration de Variables** : Maîtriser la distinction critique entre **`const`** (valeurs immuables, sauf pour les propriétés d'objets) et **`let`** (variables réassignables). Interdiction d'utiliser l'obsolète `var`.
  * **Types de Données** : Manipuler les types de base (nombres, chaînes, `undefined`, `NaN`).
  * **Conversion de Type** : Utiliser des fonctions comme `parseInt()` pour gérer les arguments passés au script et gérer les cas d'erreur (`NaN`).

## **II. Structures de Contrôle et Fonctions**

  * **Arguments de Ligne de Commande** : Accéder et analyser les arguments passés à Node.js *via* l'objet global **`process.argv`**.
  * **Conditions** : Utiliser les structures **`if...else`** pour prendre des décisions basées sur le nombre et la validité des arguments.
  * **Boucles** : Utiliser les boucles **`for`** et **`while`** pour l'itération, notamment pour imprimer des séquences ou des carrés.
  * **Fonctions** : Définir et utiliser des fonctions simples, y compris la compréhension du concept de **valeur de retour implicite (`undefined`)** et l'implémentation de la **récursivité** (pour le calcul factoriel).
  * **Modules** : Exporter des fonctions pour les rendre utilisables dans d'autres scripts *via* **`require()`** (mécanisme de base d'import/export en Node.js).

## **III. Manipulation des Objets (Rappel OOP)**

  * **Objets Littéraux** : Déclarer et manipuler des objets simples (équivalents aux dictionnaires en Python), y compris la modification des propriétés d'un objet déclaré avec **`const`** (car l'objet lui-même est mutable, même si la référence `const` ne l'est pas).

-----

# 💻 **Environnement et Exigences Techniques**

  * **Interpréteur** : Node.js (v14.x) sur Ubuntu 20.04 LTS.
  * **Convention de Code** : **`semistandard`** (Standard JS + points-virgules). **La propreté du code est non négociable.**
  * **Exigence Critique** : L'utilisation de **`var`** est strictement interdite.

-----

# 📝 **Répartition des Tâches Clés**

| Tâche | Concept JS Appliqué | Note d'Importance |
| :--- | :--- | :--- |
| **0 - 1** | `const`, `console.log()` | Syntaxe de base. |
| **2 - 4** | `process.argv`, `length`, `undefined` | Manipulation des arguments CLI. |
| **5, 7 - 8** | `parseInt()`, gestion `NaN`, `for/while` | Conversion, gestion d'erreur, boucles. |
| **9, 13** | Déclaration de fonction, `export` | **Modularité et Réutilisabilité.** |
| **10** | **Récursivité** | Maîtrise d'un concept algorithmique clé. |
| **11** | Algorithme de tri/recherche (Second Biggest) | Manipulation d'arguments comme tableau. |
| **12** | `const` sur Objet | Compréhension de la **mutabilité** d'un objet `const`. |

-----

# ✍️ **Auteur**

[Mathieu GODALIER](https://github.com/Mathieu7483) - Élève en programmation à la Holberton School

-----

# ⚖️ **Licence**

Ce projet est sous licence MIT. Pour plus de détails, consultez le fichier `LICENSE`.