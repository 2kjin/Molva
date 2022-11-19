<template>
  <div class="col">
    <div class="card border-light border-opacity-50 mb-3 bg-dark text-white img_size">
      <img :src='movieImg(movieProps.poster_path)' class="card-img-top" alt="">
      <div class="card-body">
        <h5 class="card-title txt_title">
        {{ movieProps.title }}
        </h5>
        <hr>
        <div v-for="(actor, key) in actors" :key="key">
          {{ actor }}
        </div>
        <hr>
        <div v-for="(genre, key) in genres" :key="key">
          {{ genre }}
        </div>
        <hr>
          {{ movieProps.directors[0].name }}
        <hr>
        <p class="card-text txt_post">
          {{ movieProps.overview }}
        </p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "MovieCard",
  data () {
    return {
      actors: [],
      genres: [],
    }
  },
  props: {
    movieProps : Object,
  },
  methods: {
    movieImg(img) {
      return `https://image.tmdb.org/t/p/w300/${img}`
    },
    getData () {
      const movieProps = this.movieProps
      const actorList = movieProps.actors
      const genreList = movieProps.genres
      
      for (const actor of actorList) {
        this.actors.push(actor.name)
        // console.log(actor.name)
      }
      for (const genre of genreList) {
        this.genres.push(genre.name)
        // console.log(genre.name)
      }
    }
  },
  created () {
    this.getData()
  }
}
</script>

<style>

</style>