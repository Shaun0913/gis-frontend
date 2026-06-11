import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import MapView from '../views/MapView.vue'
// 👇 这里改成 LeafletPage
import LeafletPage from '../views/LeafletPage.vue'
import MapLibreMap from '../views/MapLibreMap.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/map',
    name: 'map',
    component: MapView
  },
  {
    path: '/leaflet',
    name: 'leaflet',
    // 👇 这里也要改成 LeafletPage
    component: LeafletPage
  },
  {
    path: '/maplibre',
    name: 'maplibre',
    component: MapLibreMap
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router