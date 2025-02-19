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
  return new Intl.DateTimeFormat('en-US', {
    hour: '2-digit',
    minute: '2-digit'
  }).format(date)
}

const handleSubmit = async () => {
  if (!userInput.value.trim()) return
  
  // Add user message
  messages.value.push({
    id: Date.now(),
    type: 'user',
    content: userInput.value,
    timestamp: new Date()
  })
  
  isLoading.value = true
  
  try {
    const response = await fetch("/api/chat/", {  // Using Vite proxy
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ prompt: userInput.value })
    })

    const data = await response.json()
    
    messages.value.push({
      id: Date.now(),
      type: 'assistant',
      content: data.response || "Sorry, I couldn't generate a response.",
      timestamp: new Date()
    })
  } catch (error) {
    console.error("Error while making API request:", error)
    messages.value.push({
      id: Date.now(),
      type: 'assistant',
      content: "Error communicating with the server.",
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
      <h1>Culinary Assistant GPT</h1>
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
              Preparing response... 🔪
            </div>
          </div>
        </div>
        
        <div v-if="messages.length === 0" class="message">
          <div class="message-assistant">
            <div class="avatar">👨‍🍳</div>
            <div class="message-content">
              Hello! I am your culinary assistant. How can I help you today? 🍽️
            </div>
          </div>
        </div>
      </div>
      
      <div class="input-area">
        <textarea 
          v-model="userInput"
          placeholder="Ask your culinary question here... 🥗"
          @keyup.enter.ctrl="handleSubmit"
        ></textarea>
        <button 
          @click="handleSubmit"
          :disabled="isLoading || !userInput.trim()"
        >
          {{ isLoading ? '👨‍🍳 Processing...' : 'Send' }}
        </button>
      </div>
    </div>
  </div>
</template>
