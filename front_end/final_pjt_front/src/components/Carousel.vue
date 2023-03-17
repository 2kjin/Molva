<template>
  <div id="carousel">
    <carousel-3d :controls-visible="true"
    :inverse-scaling="200"
    :disable3d="false"
    :space="400" :display="8"
    :height="600" autoplay>
      <slide v-for="(movie, i) in movies" 
      :index="i"
      :key="movie.id">
        <carousel-item :movie="movie"/>
      </slide>
    </carousel-3d>
  </div>
</template>

<script>
import {Carousel3d, Slide} from 'vue-carousel-3d'
import CarouselItem from './CarouselItem.vue'
export default {
  name: 'CarouselContent',
  components:{
    Carousel3d,
    Slide,
    CarouselItem
  },
  computed:{
    movies(){
      return this.$store.state.movies
      
    }
  },
}
</script>

<style scoped>

div.carousel-3d-container {
  background: none;
  overflow: visible;
}
div.carousel-3d-slide{
  border-radius: 10px;
  border:none;
  transition: transform .5s;
  box-shadow: 0 10px 15px 0 #000000;
  background: none;

}
div.carousel-3d-slide:hover{
  cursor: pointer;
}
</style>