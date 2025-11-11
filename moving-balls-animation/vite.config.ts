import { defineConfig } from 'vite'
import path from 'node:path'

export default defineConfig({
  base: '/moving-balls-animation/',
  resolve: {
    alias: {
      '@': path.resolve(__dirname, 'src'),
    },
  },
})
