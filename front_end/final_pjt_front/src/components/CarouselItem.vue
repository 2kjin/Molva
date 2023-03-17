<template>
  <div id="movielItem">
    <img :src="imgSrc"
    @click="goDetail(movie?.movie_id)"
    >
      <div id="movieInfo">
        {{movie.title}}
        <v-rating
        class="rating"
        background-color="amber"
        :value="movie.vote_average / 2"
        color="amber"
        dense
        half-increments
        size="16"
        style="margin: 2px 0"
      ></v-rating>
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
#movieItem{
  position: relative;
}

#movieInfo{
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction:column;
  position: absolute;
  top: 270px;
  width: 100%;
  height: 100%;
}

img{
  height: 540px;
  display: flex;
  justify-content: center;
  align-items: center;
}

</style>