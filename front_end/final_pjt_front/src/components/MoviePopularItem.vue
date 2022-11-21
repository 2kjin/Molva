<template>
  <div id="homeMovie">
    <img :src="imgSrc"
    @click="goDetail(movie.movie_id)" />
    <span class="genre"
      >{{ movie?.release_date.split("-")[0] }} /
      {{ movie?.genres[0]["name"] }}</span
    >
    <span class="movieTitle">{{ movie?.title }}</span>
  </div>
</template>

<script>
export default {
  name: "MoviePopularItem",
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

<style>
#homeMovie {
  margin: 10px 20px;
  width: 130px;
  display: flex;
  flex-direction: column;
  color: #f8f9fa;
}

#homeMovie img {
  width: 100%;
  border-radius: 10px;
  box-shadow: 3px 3px rgba(0, 0, 0, 0.205);
  transition: transform 0.5s;
}

#homeMovie img:hover {
  cursor: pointer;
  transform: scale(1.15);
}

#homeMovie span {
  margin-left: 10px;
}
#homeMovie .genre {
  color: #e0d598;
  margin-top: 10px;
  font-size: 12px;
}

#homeMovie .movieTitle {
  font-size: 14px;
  margin-bottom: 20px;
}
</style>