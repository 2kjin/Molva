<template>
  <div id="history">
    <h2>Movie History</h2>
    <hr>
    <div class=card-container>
      <div class="cardbox"
      v-for="movie in movies" :key="movie.id">
        <img class="card-img-top" :src="`https://image.tmdb.org/t/p/original${movie.backdrop_path}`">
        <h6 style="text-align:center; width: 50%;">
        {{movie.title}}</h6>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "MyHistory",
  // 유저 데이터로 가져오기 !!!
  data(){
    return {
      movies: this.$store.state.movies
    }
  }
}
</script>

<style>
.card-container{
  max-height: 28em;
  overflow: scroll;
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 25px;
  
}
.card-container::-webkit-scrollbar {
  width: 10px;
  }
  
.card-container::-webkit-scrollbar-corner{
  display:none;
}
.card-container::-webkit-scrollbar-thumb {
  background-color:#e0d598;
  border-radius: 10px;
  background-clip: padding-box;
  border: 2px solid transparent;
  box-shadow: inset 0 0 2px #e0d598;
}
.cardbox{
  border-radius: 10px;
  border: 1px solid #f8f9facc;
  color: #F8F9FA;
  display: flex;
  margin-bottom: 10px;
  align-items: center;;
}
.cardbox img{
  border-radius: 10px 0 0 10px;
  width: 50%;
  
}
</style>