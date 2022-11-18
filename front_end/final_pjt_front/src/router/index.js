import Vue from 'vue'
import VueRouter from 'vue-router'
import IndexPage from '@/views/IndexPage'
import HomePage from '@/views/HomePage'
import MovieList from '@/views/MovieList'
import MyProfile from '@/views/MyProfile'
import SignUpPage from '@/views/SignUpPage'
import LoginPage from '@/views/LoginPage'
import CommunityPage from '@/views/CommunityPage'
import CreatePage from '@/views/CreatePage'
import DetailPage from '@/views/DetailPage'

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
  {
    path: '/community',
    name: 'CommunityPage',
    component: CommunityPage
  },
  {
    path: '/:id',
    name: 'DetailPage',
    component: DetailPage
  },
  {
    path: '/create',
    name: 'CreatePage',
    component: CreatePage
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
