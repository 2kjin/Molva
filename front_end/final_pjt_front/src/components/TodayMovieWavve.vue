<template>
  <div>
    <h4>wavve Top 10</h4>
    <TodayMovieWavveItem
      :ott-movie="ottData"
    />
  </div>
</template>

<script>
import TodayMovieWavveItem from "@/components/TodayMovieWavveItem"
export default {
  name: 'TodayMovieWavve',
  components: {
    TodayMovieWavveItem,
  },
  methods: {
    getOttMovie() {
      this.$store.dispatch('getOttMovie', 356)
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