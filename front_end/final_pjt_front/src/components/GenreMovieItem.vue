<template>
  <div>
    <!-- <div v-for="(movie,key) in gogoSing" :key="key"> -->
      <MovieLists :movieList="gogoSing"></MovieLists>
      <!-- <MovieText :text="'Popular'"></MovieText>     -->
    <!-- </div> -->
  </div>
</template>

<script>
import _ from "lodash"
// import MovieText from "../components/MovieText";
import MovieLists from "../components/MovieLists";

export default {
  name: 'GenreMovieItem',
  data() {
    return {
      randomGenreMovie: null
    }
  },
  components: {
    // MovieText,
    MovieLists,
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