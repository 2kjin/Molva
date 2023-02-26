<template>
  <div>
    <h4 style="margin: 2% 0px;" > Today's Disney Plus</h4>
    <TodayMovieDisneyItem
      :ott-movie="ottData"
      style="margin: 3% 0px;"
    />
    <!-- {{ottData}} -->
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
      return this.$store.state.ott_disney_movies
    }
  }
}
</script>

<style>

</style>