<template>
  <div>
    <h1 id="banner">  I’M JUST EXACTLY WHAT I'VE WANTED TO BE </h1>
    <carousel-content />
  </div>
</template>

<script>
import CarouselContent from "@/components/Carousel.vue"
export default {
  name: "HomeView",
  components: {
    CarouselContent,
  },
  // beforeCreate() {
  //   this.$store.dispatch("getMovies") // main
  //   // this.$store.dispatch("getMovies", "popular") // popular
  // },
}
</script>

<style scoped>
div {
  margin: 0 auto;
  max-width: 900px;
}
#banner {
  margin-top: 70px;
  text-align: center;
  color: #e0d598;
  transition: transform 0.5s linear;
}
#banner:hover {
  transform: scale(1.1);
}
</style>