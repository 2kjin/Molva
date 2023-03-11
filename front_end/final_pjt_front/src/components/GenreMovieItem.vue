<template>
  <div>
    <!-- <div v-for="(movie,key) in gogoSing" :key="key"> -->
      <GenreMovieItemList :movieList="gogoSing"></GenreMovieItemList>
      <!-- <MovieText :text="'Popular'"></MovieText>     -->
    <!-- </div> -->
  </div>
</template>

<script>
import _ from "lodash"
// import MovieText from "../components/MovieText";
import GenreMovieItemList from "../components/GenreMovieItemList";

export default {
  name: 'GenreMovieItem',
  data() {
    return {
      randomGenreMovie: null
    }
  },
  components: {
    // MovieText,
    GenreMovieItemList,
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
      return _.sampleSize(this.genreSel.data, 8)
    }
  }
}
</script>

<style>

</style>