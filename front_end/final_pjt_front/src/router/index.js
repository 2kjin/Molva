import Vue from 'vue'
import VueRouter from 'vue-router'
import IndexPage from '@/views/IndexPage'
import HomeView from '@/views/HomeView'
import DetailView from '@/views/DetailView'
import BlogView from '@/views/BlogView'
import NotFound404 from '@/views/NotFound404'


Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'IndexPage',
    component: IndexPage
  },
  {
    path: '/home',
    name: 'home',
    component: HomeView,
  },
  {
    path: '/detail/:id',
    name:'DetailView',
    component: DetailView,
  },
  {
    path:"/search",
    name:"Search",
    component:Search
  },
  {
    // username dynamic params => /:str
    path: '/blog',
    name: 'blog',
    component: BlogView,
  },
  {
    path: '/404-not-found',
    name: 'NotFound404',
    component: NotFound404,
  },
  {
    path: '*',
    redirect: { name: 'NotFound404' },
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
