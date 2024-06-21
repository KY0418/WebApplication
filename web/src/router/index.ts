import { createRouter, createWebHistory } from 'vue-router'
import type { RouteRecordRaw } from 'vue-router'
import Header from '@/layouts/Header.vue'
import Login from '@/views/Login.vue'

const routeSettings : RouteRecordRaw[] = [
  {
    path: '/',
    name: 'home',
    component: Login
  },
]

const router = createRouter({
  history: createWebHistory('App'),
  routes: routeSettings
})


export default router
