import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [vue()],
  server: {
    host: '0.0.0.0', // Permet d'accéder au serveur depuis un autre appareil sur le réseau
    port: 5173, // Port du serveur de développement
    proxy: {
      '/api': {
        target: 'http://127.0.0.1:8000', // URL de l'API FastAPI
        changeOrigin: true,
        secure: false,
      },
    },
  },
})

