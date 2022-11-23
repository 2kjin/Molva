<template>
  <div>
    <h4> Wavve Top 10</h4>
    <div v-for="(movie,key) in ottMovie" :key="key">
      {{ movie.title }}
    </div>
    <!-- {{ ottMovie }} -->
  </div>
</template>

<script>
export default {
  name: 'TodayMovieWavve',
  methods: {
    getOttMovie() {
      this.$store.dispatch('getOttMovie', '356')
    },
  },
  created() {
    this.getOttMovie()
  },
  computed: {
    ottMovie(){
      const check = this.$store.state.ott_movies
      console.log(check)
      return check
    }
  }
}
</script>

<style>

</style>