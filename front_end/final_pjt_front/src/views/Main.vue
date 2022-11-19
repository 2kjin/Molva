<template>
  <div>
    <div class="d-flex flex-wrap" v-if="nowPlaying">
      <div class="h4 ml-3 mt-5 mb-4 text-white">Now Playing</div>
      <MovieLists :movieList="nowPlaying"></MovieLists>
      <MovieText :text="'Popular'"></MovieText>
      <MovieLists :movieList="popular"></MovieLists>
      <!-- <div class="h4 ml-3 mt-5 mb-4 text-white">Comming Soon</div> -->
      <MovieText :text="'Comming Soon'"></MovieText>
      <MovieLists :movieList="upComming"></MovieLists>
      <!-- <MovieLists :movieList="movieList"></MovieLists> -->
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
import MovieLists from "../components/MovieLists";
import MovieText from "../components/MovieText";
import { movieApi } from "../utils/axios";
import { mapMutations } from "vuex";
export default {
  data() {
    return {
      nowPlaying: {},
      popular: {},
      upComming: {},
    };
  },
  components: {
    // MovieCard,
    MovieText,
    MovieLists,
  },
  methods: {
    ...mapMutations(["SET_LOADING"]),
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
      console.log(data.results);
      this.movieList = data.results;
      const { nowPlaying, popular, upComing } = movieApi;
      const requestArr = [nowPlaying, popular, upComing];
      const [now, pop, up] = await Promise.all(
        requestArr.map((li) => li().then((res) => res.data.results))
      );
      console.log("pop");
      console.log(pop);
      this.SET_LOADING(false);
      this.nowPlaying = now;
      this.popular = pop;
      this.upComming = up;
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