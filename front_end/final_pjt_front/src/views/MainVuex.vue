<template>
  <div>
    <div class="d-flex flex-wrap" v-if="movieList">
      <MovieListsVuex></MovieListsVuex>
      <!-- <div
        class="movie-card"
        style="width:125px;"
        v-for="li in movieList"
        :key="li.id"
      >
        <movie-card :li="li" :image="image"></movie-card>
      </div> -->
    </div>
  </div>
</template>

<script>
// import MovieCard from "../components/MovieCard";
import MovieListsVuex from "../components/MovieListsVuex";
import { movieApi } from "../utils/axios";
import { mapMutations } from "vuex";
export default {
  data() {
    return {
      movieList: {},
    };
  },
  components: {
    // MovieCard,
    MovieListsVuex,
  },
  methods: {
    ...mapMutations(["SET_LOADING", "SET_NOW_PLAYING", "SET_POPULAR", "SET_UP_COMING"]),
    // image(img) {
    //   return `https://image.tmdb.org/t/p/w300/${img}`;
    // },
  },
  created() {
    this.SET_LOADING(true);
  },
  async mounted() {
    try {
      // vuex를 통해서 로딩을 없애준다.
      const { data } = await movieApi.nowPlaying();
      this.SET_LOADING(false);
      console.log(data.results);
      // this.movieList = data.results;
      this.SET_NOW_PLAYING(data.results);

      const { nowPlaying, popular, upComing } = movieApi;
      const requestArr = [nowPlaying, popular, upComing];
      const [now, pop, up] = await Promise.all(
        requestArr.map((li) => li().then((res) => res.data))
      );
      
      console.log(now, pop, up);
    
    } catch (error) {
      this.movieList = "해당 자료가 존재하지 않습니다.";
    }
  },
};
</script>

<style>
.movie-card {
  margin: 12px;
  width: 125px;
  font-size: 12px;
  font-weight: 400;
}
.movie-card:hover {
  opacity: 0.5;
  cursor: pointer;
}
.movie-card > img {
  height: 180px;
  border-radius: 8px;
}
.movie-information {
  margin-top: 7px;
}

.movie-date {
  font-size: 10px;
  margin-top: 5px;
  color: #cccccc;
}
</style>
