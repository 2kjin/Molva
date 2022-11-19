<template>
  <div id="homeMovie">
    <img :src="imgSrc"
    @click="goDetail(movie.movie_id)"/>
    <span class="genre"
      >{{ movie.release_date.split("-")[0] }} /
      {{ movie.genres[0]["name"] }}</span
    >
    <span class="movieTitle">{{ movie.title }}</span>
  </div>
</template>

<script>
export default {
  name: "MovieRecentItem",
  data() {
    return {
      imgSrc: `https://image.tmdb.org/t/p/original${this.movie.poster_path}`,
    }
  },
  props: {
    movie: Object,
  },
  methods:{
    goDetail(movieId){
      this.$router.push({name:'DetailView', params:{id:movieId}})
    }
  }
}
</script>

<style></style>