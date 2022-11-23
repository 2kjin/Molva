<template>
  <div>
    <h4>Watcha Top 10</h4>
    <div v-for="(movie,key) in ottMovie" :key="key">
      {{ movie.title }}
    </div>
    <!-- {{ ottMovie }} -->
  </div>
</template>

<script>
export default {
  name: 'TodayMovieWatcha',
  methods: {
    getOttMovie() {
      this.$store.dispatch('getOttMovie', '97')
    },
  },
  created() {
    this.getOttMovie()
  },
  computed: {
    ottMovie(){
      console.log(1111111111111111111)
      const check = this.$store.state.ott_movies
      console.log(check)
      return check
    }
  }
}
</script>

<style>

</style>