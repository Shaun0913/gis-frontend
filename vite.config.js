import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [vue()],
  // 预打包依赖，提升页面加载速度
  optimizeDeps: {
    include: ['vue', 'vue-router', 'pinia', 'ol']
  }
})