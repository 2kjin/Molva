<template>
  <div>
    <div class="contanier" style="margin: 2% 0 0 0;">
      <span class="form-btn float-right" style="margin: 0px 0px 5px 0px" @click="selectGenre" >CLICK⭐</span> <br>
      <div v-if ="movielst">
        <div v-for="(movie,key) in movielst" :key="key">
          <!-- {{movie}} -->
          <p>{{ genreName[key].name }}</p>
          <hr>
          <GenreMovieItem
            :genre-sel="movie"
          />
          <br>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import _ from "lodash"
import axios from "axios"
import router from '@/router'
import GenreMovieItem from '@/components/GenreMovieItem'

const API_URL = "http://127.0.0.1:8000"

export default {
  name: 'GenreMovie',
  data () {
    return {
      movielst:[],
      genreName: []
    }
  },
  components: {
    GenreMovieItem,
  },
  methods: {
    getGenreMenu() {
      this.$store.dispatch('getGenreMenu')
    },
    selectGenre() {
      const chk = (_.sampleSize(this.$store.state.genre_menu, 5))
      this.genreName = chk
      this.movielst = []
      const tmp_lsit = []
      chk.forEach( genre =>
        axios({
          method: "get",
          url: `${API_URL}/movies/create_genre_list/${genre.genre_id}/`,
        })
          .then((res) => {
            tmp_lsit.push(res)
          })
          .catch((err)=>{
            router.push('/404-not-found')
            console.log(err)
          })
      )
      this.movielst = tmp_lsit

    }
  },
  created() {
    this.getGenreMenu()
  },
}
</script>
