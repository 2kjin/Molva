<template>
  <div id="carouselItem">
    <!-- <img :src="imgSrc"> -->
    <img :src="imgSrc" @click="goDetail(movie?.movie_id)">
      <div id="carouselContent">
        <!-- <v-rating
        class="rating"
        background-color="amber"
        :value="movie.vote_average / 2"
        color="amber"
        dense
        half-increments
        readonly
        size="18"
        style="margin: 3px 0"
      ></v-rating> -->
    </div>
    
  </div>
</template>

<script>
export default {
  name:'CarouselItem',
  computed:{
    imgSrc(){
      return `https://image.tmdb.org/t/p/original${this.movie.poster_path}`
    }
  },
  props:{
    movie:Object,
  },
  methods:{
    goDetail(movieId){
      this.$router.push({name:'DetailView', params:{id:movieId}})
    }
  }
}
</script>

<style scoped>

#carouselItem{
  display: flex;
}

img{
  width: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
}

/* more button */
/* button:hover{
  cursor: pointer;
  transform: scale(1.4);
} */

</style>