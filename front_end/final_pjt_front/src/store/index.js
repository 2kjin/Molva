import Vue from "vue"
import Vuex from "vuex"
import axios from "axios"
import createPersistedState from "vuex-persistedstate"
import router from '@/router'

const API_URL = "http://127.0.0.1:8000"

Vue.use(Vuex)

export default new Vuex.Store({
  plugins:[
    createPersistedState(),
  ],
  state: {
    token: null,
    movies: null,
    movie:null,
    loading: true,
  },
  getters: {
    isLogin(state) {
      return state.token ? true : false
    }
  },
  mutations: {
    SET_LOADING(state, data){
      state.loading = data;
    },
    SAVE_TOKEN(state, token) {
      state.token = token
      router.push({ name: 'home' })
    },
    LOG_OUT(state) {
      state.token = null
      router.push({ name: 'home' })
    },
    GET_MOVIES(state, payload) {
        state.movies = payload.movies
    },
    GET_DETAIL(state, payload) {
      state.movie = payload
    }
  },
  actions: {
    // 회원가입
    signUp(context, payload) {
      const username = payload.username
      const password1 = payload.password1
      const password2 = payload.password2

      axios({
        method: "post",
        url: `${API_URL}/accounts/signup/`,
        data: {
          username,
          password1,
          password2,
        },
      })
        .then((res) => {
          context.commit("SAVE_TOKEN", res.data.key)
          
        })
        .catch((err) => {
          console.log(err)
        })
    },
    // 로그인
    login(context, payload) {
      const username = payload.username
      const password = payload.password
      
      axios({
        method: "post",
        url: `${API_URL}/accounts/login/`,
        data: {
          username,
          password,
        }
      })
      .then((res) => {
        context.commit("SAVE_TOKEN", res.data.key)
      })
      .catch((err) => {
        console.log(err)
      })
    },
    // 로그아웃
    logOut(context) {
      axios({
        method: "post",
        url: `${API_URL}/accounts/logout/`,
      })
      .then((res) => {
        context.commit("LOG_OUT", res.data.key)
      })
      .catch((err) => {
        console.log(err)
      })
    },
    // GET_MOVIES
    getMovies(context, payload) {
      let params = null

      if (payload) {
        params = {
          sorted: payload,
        }
      }

      axios({
        method: "get",
        url: `${API_URL}/movies/`,
        params: params,
      })
        .then((res) => {
          const moviePayload = {
            sorted: payload,
            movies: res.data,
          }
          context.commit("GET_MOVIES", moviePayload)
        })
        .catch((err) => {
          console.log(err)
        })
    },
    // GET MOVIE DETAIL
    getDetail(context, movieId){
      axios({
        method: "get",
        url: `${API_URL}/movies/${movieId}/`,
      })
        .then((res)=>{
          context.commit("GET_DETAIL", res.data)
        })
        .catch((err)=>{
          router.push('/404-not-found')
          console.log(err)
          
        })

    }
  },
  modules: {},
})