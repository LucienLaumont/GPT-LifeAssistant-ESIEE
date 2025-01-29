<script setup lang="ts">
import { ref } from 'vue'

interface Message {
  id: number
  type: 'user' | 'assistant'
  content: string
  timestamp: Date
}

const userInput = ref('')
const messages = ref<Message[]>([])
const isLoading = ref(false)

const formatTime = (date: Date) => {
  return new Intl.DateTimeFormat('fr-FR', {
    hour: '2-digit',
    minute: '2-digit'
  }).format(date)
}

const handleSubmit = async () => {
  if (!userInput.value.trim()) return
  
  // Ajouter le message de l'utilisateur
  messages.value.push({
    id: Date.now(),
    type: 'user',
    content: userInput.value,
    timestamp: new Date()
  })
  
  isLoading.value = true
  
  try {
    const response = await fetch("/api/chat/", {  // Utilisation du proxy Vite
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ prompt: userInput.value })
    })

    const data = await response.json()
    
    messages.value.push({
      id: Date.now(),
      type: 'assistant',
      content: data.response || "Désolé, je n'ai pas pu générer une réponse.",
      timestamp: new Date()
    })
  } catch (error) {
    console.error("Erreur lors de la requête API :", error)
    messages.value.push({
      id: Date.now(),
      type: 'assistant',
      content: "Erreur de communication avec le serveur.",
      timestamp: new Date()
    })
  }

  isLoading.value = false
  userInput.value = ''
}
</script>

<template>
  <div class="container">
    <div class="header">
      <div class="header-icons">
        🥘 🍳 👨‍🍳 🥗
      </div>
      <h1>Assistant Culinaire GPT</h1>
    </div>
    
    <div class="chat-container">
      <div class="chat-history">
        <div v-for="message in messages" :key="message.id" class="message">
          <div :class="['message-' + message.type]">
            <div class="avatar">
              {{ message.type === 'user' ? '👤' : '👨‍🍳' }}
            </div>
            <div class="message-content">
              {{ message.content }}
              <div class="timestamp">{{ formatTime(message.timestamp) }}</div>
            </div>
          </div>
        </div>
        
        <div v-if="isLoading" class="message">
          <div class="message-assistant">
            <div class="avatar">👨‍🍳</div>
            <div class="message-content">
              Préparation de la réponse... 🔪
            </div>
          </div>
        </div>
        
        <div v-if="messages.length === 0" class="message">
          <div class="message-assistant">
            <div class="avatar">👨‍🍳</div>
            <div class="message-content">
              Bonjour ! Je suis votre assistant culinaire. Comment puis-je vous aider aujourd'hui ? 🍽️
            </div>
          </div>
        </div>
      </div>
      
      <div class="input-area">
        <textarea 
          v-model="userInput"
          placeholder="Posez votre question culinaire ici... 🥗"
          @keyup.enter.ctrl="handleSubmit"
        ></textarea>
        <button 
          @click="handleSubmit"
          :disabled="isLoading || !userInput.trim()"
        >
          {{ isLoading ? '👨‍🍳 En cours...' : 'Envoyer' }}
        </button>
      </div>
    </div>
  </div>
</template>
