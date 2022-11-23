<template>
  <div>
    <h4>Disney Plus Top 10</h4>
    <TodayMovieDisneyItem
      :ott-movie="ottData"
    />
  </div>
</template>

<script>
import TodayMovieDisneyItem from "@/components/TodayMovieDisneyItem"
export default {
  name: 'TodayMovieDisney',
  components: {
    TodayMovieDisneyItem,
  },
  methods: {
    getOttMovie() {
      this.$store.dispatch('getOttMovie', 337)
    }
  },
  created() {
    this.getOttMovie()
  },
  computed:{
    ottData() {
      return this.$store.state.ott_movies
    }
  }
}
</script>

<style>

</style>