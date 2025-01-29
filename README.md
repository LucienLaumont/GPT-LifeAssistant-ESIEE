# GPT-LifeAssistant-ESIEE

## Description
GPT-LifeAssistant-ESIEE est un projet développé à l'ESIEE qui utilise l'intelligence artificielle pour créer un assistant de vie. Ce projet combine plusieurs technologies, notamment Jupyter Notebook, Vue.js, CSS et Python, pour offrir une solution complète d'assistance personnelle.

## Motivation
La motivation derrière ce projet est de démontrer comment les technologies d'intelligence artificielle peuvent être utilisées pour améliorer la vie quotidienne. L'objectif est de créer un assistant personnel capable de répondre à diverses questions, fournir des recommandations et effectuer des tâches courantes de manière efficace et intuitive.

## Objectifs
- **Développer un assistant personnel basé sur l'IA** : Créer un assistant capable de répondre intelligemment aux questions des utilisateurs.
- **Créer une interface utilisateur intuitive** : Développer une interface web user-friendly avec Vue.js et CSS.
- **Analyser les données pour fournir des réponses pertinentes** : Utiliser Python pour analyser les données et entraîner les modèles d'IA.
- **Intégrer diverses technologies** : Démontrer l'utilisation de différentes technologies et leur synergie dans un projet cohérent.

## Architecture du Projet
L'architecture du projet est divisée en plusieurs composants principaux :

1. **Backend (Python, Jupyter Notebook)** :
   - Responsable de l'analyse des données et de la génération des réponses.
   - Utilise des modèles d'IA pour traiter les requêtes des utilisateurs.
   - Scripts Python pour le prétraitement des données et l'entraînement des modèles.

2. **Frontend (Vue.js, CSS)** :
   - Interface utilisateur pour interagir avec l'assistant.
   - Utilise Vue.js pour créer une application web réactive.
   - CSS pour le stylisme et la mise en page de l'interface.

3. **Base de données** :
   - Stockage des données nécessaires pour l'assistant.
   - Utilisation d'une base de données relationnelle pour un accès rapide et efficace aux informations.


## Installation

### Prérequis
- **Python 3.x** : Pour exécuter les scripts backend et Jupyter Notebook.
- **Node.js** : Pour exécuter le serveur web et les dépendances frontend.
- **Jupyter Notebook** : Pour travailler avec les notebooks interactifs.

### Étapes d'installation
1. Clonez le dépôt :
    ```bash
    git clone https://github.com/LucienLaumont/GPT-LifeAssistant-ESIEE.git
    ```

2. Installez les dépendances :
    - Pour les notebooks Jupyter :
        ```bash
        pip install -r requirements.txt
        ```
    - Pour l'interface web :
        ```bash
        npm install
        ```

## Utilisation

### Lancer le Serveur Web
1. Lancez le serveur web pour l'interface utilisateur :
    ```bash
    npm run serve
    ```

### Exécuter les Notebooks Jupyter
1. Ouvrez les notebooks Jupyter pour exécuter les scripts Python :
    ```bash
    jupyter notebook
    ```
2. Naviguez vers le répertoire contenant les notebooks et ouvrez-les pour commencer à travailler avec les modèles d'IA.

## Détails d'Implémentation

### Backend
- **Analyse des données** : Les données sont prétraitées en utilisant des scripts Python pour les rendre aptes à l'entraînement des modèles d'IA.
- **Modèles d'IA** : Utilisation de bibliothèques telles que TensorFlow et scikit-learn pour entraîner des modèles capables de répondre aux questions des utilisateurs.
- **API** : Développement d'une API RESTful pour permettre à l'interface utilisateur de communiquer avec le backend.

### Frontend
- **Vue.js** : Utilisé pour créer une interface utilisateur réactive et dynamique.
- **Composants** : Développement de composants réutilisables pour différentes parties de l'interface, comme le champ de recherche, les boutons, etc.
- **CSS** : Stylisme de l'interface pour une expérience utilisateur agréable.

### Base de Données
- **Stockage** : Utilisation d'une base de données relationnelle pour stocker les données utilisateur et les informations nécessaires pour l'assistant.
- **Requêtes** : Optimisation des requêtes pour un accès rapide aux données.

## Résultats

### Tests et Performances
- **Précision** : Les tests montrent que l'assistant est capable de répondre avec précision à une variété de questions grâce à l'entraînement des modèles d'IA.
- **Réactivité** : L'interface utilisateur est rapide et réactive, offrant une bonne expérience utilisateur.

### Exemple de Réponses
- **Question** : "Quel temps fait-il aujourd'hui ?"
  - **Réponse** : "Il fait ensoleillé avec une température de 25°C."
- **Question** : "Peux-tu me recommander un restaurant à proximité ?"
  - **Réponse** : "Je vous recommande le restaurant 'Le Gourmet' situé à 500m de votre position actuelle."

## Conclusion
GPT-LifeAssistant-ESIEE démontre l'efficacité de l'intelligence artificielle pour améliorer la vie quotidienne. Le projet a atteint ses objectifs principaux et ouvre la voie à de futures améliorations et fonctionnalités.

## Contribution
Les contributions sont les bienvenues ! Veuillez soumettre des pull requests avec des descriptions détaillées des modifications.


## Auteurs
- Lucien Laumont
- Théo Lindqvist
- Théo Labat

## Remerciements
Merci à tous ceux qui ont contribué à ce projet.
