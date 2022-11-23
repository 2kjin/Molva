<template>
  <div>
    <h4 style="margin: 2% 0px;">Watcha Top 10</h4>
    <TodayMovieWatchaItem
      :ott-movie="ottData"
      style="margin: 3% 0px;"
    />
  </div>
</template>

<script>
import TodayMovieWatchaItem from "@/components/TodayMovieWatchaItem"
export default {
  name: 'TodayMovieWatcha',
  components: {
    TodayMovieWatchaItem,
  },
  methods: {
    getOttMovie() {
      this.$store.dispatch('getOttMovie', 97)
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