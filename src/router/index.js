import { createRouter, createWebHashHistory } from 'vue-router'
import Homepage from '../views/Homepage.vue'
import AboutPage from '../views/AboutPage.vue'

const routes = [
  {
    path: '/',
    name: 'Homepage',
    component: Homepage
  },

  {
    path: '/about',
    name: 'AboutPage',
    component: AboutPage
  },

  {
    path: '/anime/:id',
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
