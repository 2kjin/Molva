import Vue from "vue"
import Vuex from "vuex"
import axios from "axios"
// 일단 comment 완성하려고 토큰 저장
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
    moviesPopular: null,
    moviesRecent: null,
    loading: true,

  },
  getters: {},
  mutations: {
    SET_LOADING(state, data){
      state.loading = data;
    },
    SAVE_TOKEN(state, token) {
      state.token = token
    },
    GET_MOVIES(state, payload) {
      const sortValue = payload.sorted

      if (sortValue === undefined) {
        state.movies = payload.movies
      } else if (sortValue === "popular") {
        state.moviesPopular = payload.movies
      } else if (sortValue === "recent") {
        state.moviesRecent = payload.movies
      }
    },
    GET_DETAIL(state, payload) {
      state.movie = payload
    }
  },
  actions: {
    // SIGN_UP
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
          // 생성된 토큰 넘겨주기
          context.commit("SAVE_TOKEN", res.data.key)
        })
        .catch((err) => {
          console.log(err)
        })
    },
    // Login
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