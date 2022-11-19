<template>
  <div>
    <movie-popular-item
      v-for="movie in movies"
      :key="movie.id"
      :movie="movie"
    />
  </div>
</template>

<script>
import MoviePopularItem from "./MoviePopularItem.vue"
export default {
  name: "MoviePopular",
  components: {
    MoviePopularItem,
  },
  computed: {
    movies() {
      return this.$store.state.moviesPopular
    },
  },
}
</script>

<style scoped>
div {
  display: flex;
  flex-wrap: wrap;
}
</style>