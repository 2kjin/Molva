<template>
  <div>
    <h1 id="banner">  I’M JUST EXACTLY WHAT I'VE WANTED TO BE </h1>
    <div id="carousel">
    <carousel-3d :width="350" :height="500"
    :autoplay="true" :autoplay-timeout="1800">
      <slide v-for="(movie, i) in movies" 
      :index="i"
      :key="movie.id">
        <CarouselItem :movie="movie"/>
      </slide>
    </carousel-3d>
  </div>
  </div>
</template>

<script>
import {Carousel3d, Slide} from 'vue-carousel-3d'
import CarouselItem from '@/components/CarouselItem'

export default {
  name: "HomeView",
  components: {
    Carousel3d,
    Slide,
    CarouselItem,
  },
  computed:{
    movies(){
      return this.$store.state.movies
    }
  },
}
</script>

<style scoped>
div {
  margin: 0 auto;
  max-width: 100vw;
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
#carousel{
  margin: 80px auto;
  margin-bottom: 50px;
  border-radius: 10px;
}
/* .carousel-3d {
    width: 150%;
    height: 200px;
} */
div.carousel-3d-container {
  background: none;
  overflow: visible;
}
div.carousel-3d-slide{
  border-radius: 10px;
  border:none;
  transition: transform .5s;
  box-shadow: 0 10px 15px 0 #000000;
}
div.carousel-3d-slide:hover{
  cursor: pointer;
}
</style>