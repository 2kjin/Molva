import Vue from 'vue'
import VueRouter from 'vue-router'
import IndexPage from '@/views/IndexPage'
import HomePage from '@/views/HomePage'
import MovieList from '@/views/MovieList'
import MyProfile from '@/views/MyProfile'
import SignUpPage from '@/views/SignUpPage'
import LoginPage from '@/views/LoginPage'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'IndexPage',
    component: IndexPage
  },
  {
    path: '/home',
    name: 'HomePage',
    component: HomePage
  },
  {
    path: '/movielist',
    name: 'MovieList',
    component: MovieList
  },
  {
    path: '/myprofile',
    name: 'MyProfile',
    component: MyProfile
  },
  {
    path: '/singup',
    name: 'SignUpPage',
    component: SignUpPage
  },
  {
    path: '/login',
    name: 'LoginPage',
    component: LoginPage
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
