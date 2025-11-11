import { defineConfig } from 'vite'
import path from 'node:path'

export default defineConfig({
  base: '/Rube-Goldberg-CSS-Machine/',
  resolve: {
    alias: {
      '@': path.resolve(__dirname, 'src'),
    },
  },
})
