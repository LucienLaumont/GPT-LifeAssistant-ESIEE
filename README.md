# 🍳 DailyAssistant - Assistant Culinaire GPT  

Bienvenue dans **DailyAssistant**, un assistant de cuisine basé sur un **LLM finetuné à partir de GPT-2**. Ce projet vise à vous aider à réaliser vos plats en vous fournissant des conseils et des recettes comme un véritable assistant culinaire.  

## 🏗️ Structure du projet  

Le repository est divisé en deux parties principales :  

📂 **`app/`** - Contient le code pour **exécuter le backend et le frontend** :  
- **Backend** : API développée avec **FastAPI** pour interagir avec le modèle fine-tuné.  
- **Frontend** : Interface développée avec **Vue.js** pour interagir avec l’assistant.  

📂 **`finetuning_gpt2/`** - Contient les notebooks et les données pour le **finetuning de GPT-2** :  
- **Jupyter Notebook** permettant de finetuner et tester différents modèles **GPT-2**.  
- **Données d'entraînement** utilisées pour spécialiser le modèle en tant qu'assistant culinaire.  

---

## 🚀 Installation & Configuration  

### **1️⃣ Créer un environnement virtuel**  
Dans le dossier **racine du projet**, exécutez :  
```sh
python -m venv venv
source venv/bin/activate  # Sur Mac/Linux
venv\Scripts\activate      # Sur Windows
```

### **2️⃣ Installer les dépendances**  
Dans le dossier `DailyAssistant/app/` (pour le backend) :  
```sh
pip install -r requirements.txt
```
Dans le dossier `DailyAssistant/app/project/` (pour le frontend) :  
```sh
npm install
```

---

## 🏃‍♂️ Lancer l'application  

### **1️⃣ Démarrer l'API (Backend)**  
📂 **Se placer dans le dossier `DailyAssistant/app/` et exécuter** :  
```sh
cd DailyAssistant/app
uvicorn api.main:app --reload
```
📌 **L’API est accessible sur** `http://127.0.0.1:8000/`  
📌 **Documentation interactive Swagger** : `http://127.0.0.1:8000/docs`  

---

### **2️⃣ Démarrer le Frontend (Vue.js)**  
📂 **Se placer dans le dossier `DailyAssistant/app/project/` et exécuter** :  
```sh
cd DailyAssistant/app/project
npm run dev
```
📌 **L'interface utilisateur est accessible sur** `http://localhost:5173/` (port par défaut de Vite).  

---

## 🎯 Tester le modèle  

### **Tester via l'interface frontend**
Une fois **l'API et le frontend démarrés**, ouvrez `http://localhost:5173/` et commencez à discuter avec l'assistant culinaire.  

### **Tester via un appel API (`cURL` ou Postman)**  
Vous pouvez envoyer une requête POST pour interagir avec le modèle :  
```sh
curl -X POST http://127.0.0.1:8000/api/chat/ \
-H "Content-Type: application/json" \
-d '{"prompt": "How to steam carrot?"}'
```

---

## 📌 Remarques  
- Le **modèle GPT-2** a été fine-tuné avec un corpus orienté **cuisine et gastronomie**.  
- Les réponses sont **nettoyées** et **optimisées** avec des techniques de **pré-processing avancées** (suppression des phrases incomplètes et des redondances).  
- Le projet peut être **déployé sur un serveur distant** (ex: **AWS, Docker, Nginx**) pour une utilisation en production.  

**🍽️ Bonne session cuisine avec DailyAssistant !** 🚀  
