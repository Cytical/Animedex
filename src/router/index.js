import { createRouter, createWebHashHistory } from 'vue-router'
import Homepage from '../views/Homepage.vue'
import About from '../views/About.vue'

const routes = [
  {
    path: '/',
    name: 'Homepage',
    component: Homepage
  },

  {
    path: '/about',
    name: 'About',
    component: About
  },

  {
    path: '/anime/:category/:id',
    name: 'Anime',
    props: true,
    component: () => import('../views/AnimeView.vue'),
  },
]

const router = createRouter({
  history: createWebHashHistory(process.env.BASE_URL),
  routes
})

export default router
