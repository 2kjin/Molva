<template>
  <div id="carouselItem">
    <img :src="imgSrc"
      @click="goDetail(movie?.movie_id)">
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


</style>