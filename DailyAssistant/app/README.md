# 🍽️ Assistant Culinaire GPT 🍳

Bienvenue dans **Assistant Culinaire GPT**, votre compagnon idéal en cuisine ! 🥗👨‍🍳

## 🌟 Présentation
L'Assistant Culinaire GPT est une application interactive combinant une interface utilisateur moderne avec une intelligence artificielle spécialisée en cuisine. Grâce à son modèle de langage avancé, il est capable d'apporter des conseils précis et adaptés aux besoins des utilisateurs.

## 🔥 Fonctionnalités
- **Conseils personnalisés** 📝 : Posez vos questions et obtenez des recommandations adaptées.
- **Base de données culinaire** 📚 : Consultation d’une base de connaissances enrichie avec des recettes et des astuces.
- **Interaction intuitive** 💬 : Discussion fluide avec un chatbot réactif et convivial.

## 🏗️ Architecture de l’Application
L’application est composée de deux parties principales :

### 🎨 Frontend - Vue.js
L’interface utilisateur est développée avec **Vue.js** et **Vite** pour un rendu rapide et interactif. 
- **Composant principal** : `CookingAssistant.vue` gère les échanges entre l’utilisateur et l’IA.
- **Proxy Vite** : Permet de rediriger les requêtes vers le backend pour éviter les problèmes de CORS.
- **Expérience utilisateur** : Une interface épurée et responsive avec des animations subtiles pour une meilleure immersion.

### 🧠 Backend - FastAPI
Le backend repose sur **FastAPI**, un framework performant pour les applications asynchrones en Python.
- **Serveur API** 🌍 : Gère les requêtes et la communication avec l’IA.
- **Modèle IA** 🤖 : Un modèle **LLM fine-tuné** pour comprendre et répondre aux questions culinaires.
- **Base de données JSON** 🗄️ : Contient les recettes et informations nutritionnelles pour enrichir les réponses.

## ⚙️ Déploiement & Configuration
L’application est configurée pour être accessible sur un réseau local via **Vite** pour le frontend et **FastAPI** pour le backend.

- **Port du serveur Vue.js** : `5173` (accessible sur `0.0.0.0` pour permettre l’accès depuis d’autres appareils du réseau).
- **Proxy API** : Les requêtes `/api` sont redirigées vers `http://127.0.0.1:8000`.

## 📡 Flux de Communication
1. **L’utilisateur pose une question** via l’interface Vue.js.
2. **Requête envoyée à FastAPI** via une API REST.
3. **Traitement par le modèle IA** qui analyse la requête.
4. **Réponse formatée** et renvoyée à l’interface pour affichage.

## 🚀 Conclusion
L'Assistant Culinaire GPT est conçu pour offrir une expérience fluide et immersive aux passionnés de cuisine. Grâce à l’intelligence artificielle et une interface moderne, il vous aide à explorer de nouvelles recettes, optimiser vos plats et approfondir vos connaissances culinaires. 

👨‍🍳 **À vos fourneaux, et bon appétit !** 🥘

