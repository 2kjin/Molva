<template>
  <div>
    <h4 style="margin: 2% 0px;" >Disney Plus Top 10</h4>
    <TodayMovieDisneyItem
      :ott-movie="ottData"
      style="margin: 3% 0px;"
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