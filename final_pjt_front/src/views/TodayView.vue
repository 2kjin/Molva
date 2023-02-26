<template>
  <!-- - npm install -D pug-plain-loader pug
  - npm install sass-loader sass webpack --save-dev
  - npm i lodash -->
  <div style="padding:auto; margin:auto;">
    <br>
    <br>
    <TodayMovieNetflix /><hr>
    <TodayMovieDisney/><hr>
    <TodayMovieWatcha/><hr>
    <TodayMovieWavve/>

  </div>
</template>

<script>
import TodayMovieNetflix from "@/components/TodayMovieNetflix"
import TodayMovieDisney from "@/components/TodayMovieDisney"
import TodayMovieWatcha from "@/components/TodayMovieWatcha"
import TodayMovieWavve from "@/components/TodayMovieWavve.vue"

export default {
  name: 'TodayView',
  components: {
    TodayMovieNetflix,
    TodayMovieDisney,
    TodayMovieWatcha,
    TodayMovieWavve
  },
}
</script>

<style>

</style>