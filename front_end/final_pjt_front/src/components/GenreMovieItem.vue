<template>
  <div>
    <div v-for="(movie,key) in gogoSing" :key="key">
      {{ movie.title }}
    </div>
  </div>
</template>

<script>
import _ from "lodash"

export default {
  name: 'GenreMovieItem',
  data() {
    return {
      randomGenreMovie: null
    }
  },
  props: {
    genreSel : Object,
  },
  methods: {
    randomMovie() {
      this.randomGenreMovie = _.sampleSize(this.genreSel.data, 6)
    }
  },
  computed: {
    gogoSing() {
      return _.sampleSize(this.genreSel.data, 6)
    }
  }
}
</script>

<style>

</style>