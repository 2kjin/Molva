<template>
  <div>
    <h1 id="banner1">  Welcome Molva Platform</h1>
    <h1 id="banner2">  Enjoy Your Moive </h1>
    <CarouselContent/>
    <NowMovieViewVue/>
  </div>
</template>

<script>
import CarouselContent from "@/components/Carousel.vue"
import NowMovieViewVue from "@/components/NowMovieView"
export default {
  name: "HomeView",
  components: {
    CarouselContent,
    NowMovieViewVue,
  },
  beforeCreate() {
    this.$store.dispatch("getMovies")
  },
}
</script>

<style scoped>
div {
  margin: 0 auto;
  max-width: 100vw;
}
#banner1 {
  margin-top: 40px;
  text-align: center;
  color: #e0d598;
  transition: transform 0.5s linear;
}
#banner1:hover {
  transform: scale(1.1);
}
#banner2 {
  margin-top: 10px;
  margin-bottom: 40px;
  text-align: center;
  color: #e0d598;
  transition: transform 0.5s linear;
}
#banner2:hover {
  transform: scale(1.1);
}
</style>