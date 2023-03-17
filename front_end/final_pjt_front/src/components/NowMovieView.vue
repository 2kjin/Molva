<template>
  <div class="d-flex justify-content-center">
    <div class="contentItem mx-10" v-if="nowPlaying">
      <div class="h4" style="color:#e0d598">Now Playing</div>
      <MovieLists :movieList="nowPlaying"></MovieLists>
    </div>
    <div class="contentItem mx-10" v-if="popular">
      <div class="h4" style="color:#e0d598">Popular</div>
      <MovieLists :movieList="popular"></MovieLists>
    </div>
    <div class="contentItem mx-10" v-if="upComming">
      <div class="h4" style="color:#e0d598">Comming Soon</div>
      <MovieLists :movieList="upComming"></MovieLists>
    </div>
  </div>
</template>

<script>
import MovieLists from "../components/MovieListsColumn";
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
    MovieLists,
  },
  methods: {
    ...mapMutations(["SET_LOADING"]),
  },
  
  created() {
    this.SET_LOADING(true);
  },
  async mounted() {
    try {
      // vuex를 통해서 로딩을 없애준다.
      const { data } = await movieApi.nowPlaying();
      this.movieList = data.results;
      const { nowPlaying, popular, upComing } = movieApi;
      const requestArr = [nowPlaying, popular, upComing];
      const [now, pop, up] = await Promise.all(
        requestArr.map((li) => li().then((res) => res.data.results))
      );
      // console.log("pop");
      // console.log(pop);
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
  cursor: pointer;
  transform: scale(1.1);
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