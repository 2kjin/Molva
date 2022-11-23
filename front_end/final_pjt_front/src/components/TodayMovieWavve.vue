<template>
  <div>
    <h4 style="margin: 2% 0px;">Wavve Top 10</h4>
    <TodayMovieWavveItem
      :ott-movie="ottData"
      style="margin: 3% 0px;"
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