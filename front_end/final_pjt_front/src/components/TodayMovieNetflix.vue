<template>
  <div>
    <h4 style="margin: 0px 0px 2% 0px;">Netflix Top 10</h4>
    <TodayMovieNetflixItem
      :ott-movie="ottData"
      style="margin: 3% 0px;"
    />
  </div>
</template>

<script>
import TodayMovieNetflixItem from "@/components/TodayMovieNetflixItem"
export default {
  name: 'TodayMovieNetflix',
  components: {
    TodayMovieNetflixItem,
  },
  methods: {
    getOttMovie() {
      this.$store.dispatch('getOttMovie', 8)
    }
  },
  created() {
    this.getOttMovie()
  },
  computed: {
    ottData() {
      return this.$store.state.ott_movies
    }
  }
}
</script>

<style>

</style>