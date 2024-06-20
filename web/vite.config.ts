import { fileURLToPath, URL } from 'node:url'

import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import VueDevTools from 'vite-plugin-vue-devtools'
import UnocssVitePlugin from 'unocss/vite'
import { presetAttributify,presetUno } from 'unocss'
import extractorPug from '@unocss/extractor-pug'

// https://vitejs.dev/config/
export default defineConfig({
  server: {
    host: true
  },
  plugins: [
    vue(),
    UnocssVitePlugin({
      presets: [presetAttributify(),presetUno()],
      include: [
        './index.html',
        './src/**/*.{vue,js,ts,jsx,tsx}',
        './node_modules/unocss/**/*.{vue,js,ts,jsx,tsx}'
      ],
      extractors: [extractorPug()]
    }),
    VueDevTools(),
  ],
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url))
    }
  }
})
