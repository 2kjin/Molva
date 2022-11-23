<template>
  <div>
    <h4> Disney Plus Top 10</h4>
    <div v-for="(movie,key) in ottMovie" :key="key">
      {{ movie.title }}
    </div>
    <!-- {{ ottMovie}} -->
  </div>
</template>

<script>
export default {
  name: 'TodayMovieDisney',
  methods: {
    getOttMovie() {
      this.$store.dispatch('getOttMovie', '337')
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