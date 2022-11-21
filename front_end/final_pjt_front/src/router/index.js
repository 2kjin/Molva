import Vue from 'vue'
import VueRouter from 'vue-router'
import IndexPage from '@/views/IndexPage'
import HomeView from '@/views/HomeView'
import MovieView from '@/views/MovieView'
import DetailView from '@/views/DetailView'
import MyProfile from '@/views/MyProfile'
import SearchView from '@/views/SearchView'
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
    path: '/movie',
    name: 'movie',
    component: MovieView,
  },
  {
    path: '/404-not-found',
    name: 'NotFound404',
    component: NotFound404,
  },
  {
    path: '/:id',
    name:'DetailView',
    component: DetailView,
  },
  {
    path:"/search",
    name:"search",
    component: SearchView
  },
  {
    // username dynamic params => /:str
    path: '/myprofile',
    name: 'MyProfile',
    component: MyProfile,
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
