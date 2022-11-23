<template>
  <div>
    <br>
    <TodayMovieNetflix/>
    <TodayMovieDisney/>
    <!-- <TodayMovieWatcha/> -->
    <TodayMovieWavve/>

  </div>
</template>

<script>
import TodayMovieNetflix from "@/components/TodayMovieNetflix.vue"
import TodayMovieDisney from "@/components/TodayMovieDisney.vue"
// import TodayMovieWatcha from "@/components/TodayMovieWatcha.vue"
import TodayMovieWavve from "@/components/TodayMovieWavve.vue"

export default {
  name: 'TodayView',
  components: {
    TodayMovieNetflix,
    TodayMovieDisney,
    // TodayMovieWatcha,
    TodayMovieWavve
  },
}
</script>

<style>

</style>