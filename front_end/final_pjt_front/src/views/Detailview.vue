<template>
<div style="padding: 0 auto;">
  <div class="movie-detail" v-if="movieDetail && movieDetail.backdrop_path">
    <div
      class="movie-detail-image"
      :style="{ backgroundImage: `url(${image(movieDetail.backdrop_path)})` }"
    ></div>
    <div class="movie-content d-flex">
      <div style="">
        <img
          class="mt-2"
          style="height:60vh; border-radius: 10px;"
          :src="image(movieDetail.poster_path)"
        />
      </div>
      <div class="ml-4 w-75">
        <h1 class="movie-title">{{ movieDetail.title }}</h1>
        <div class="movie-information-wrapper mt-4 d-flex align-items-center">
          <div>{{ movieDetail.release_date.split("-")[0] }}</div>
          <span class="ml-1">ㆍ</span>
          <div>{{ movieDetail.runtime }} 분</div>
          <span class="ml-1">ㆍ</span>
          <div class="ml-2 d-flex">
            <div
              class="genres"
              v-for="genre in movieDetail.genres"
              :key="genre.id"
            >
              {{ genre.name }}
            </div>
            <span class="ml-1">ㆍ</span>
            <v-rating
            style="display:inline-block; margin-bottom: 5px;"
            class="rating"
            background-color="amber"
            :value="movieDetail.vote_average/2"
            color="amber"
            dense
            half-increments
            readonly
            size="22"
          ></v-rating>
          </div>
        </div>
        <div class="movie-information-wrapper mt-4 d-flex align-items-center">
        <div>{{ movieDetail.actors }}</div>
        </div>
        <div class="movie-overview mt-3">{{ movieDetail.overview }}</div>
        <div v-if="movieDetail.videos && movieDetail.videos.results">
          <iframe
          v-if="movieDetail.videos.results[0]"
            class="mt-5"
            :key="movieDetail.videos.results[0].key"
            width="640"
            height="360"
            :src="youtube(movieDetail.videos.results[0].key)"
            frameborder="0"
            allow=" fullscreen "
          >
          </iframe>
        </div>
        <!-- </div> -->
      </div>
    </div>
  </div>
</div>
</template>

<script>
import { movieApi } from "../utils/axios";
import { mapMutations } from "vuex";
export default {
  data() {
    return {
      movieDetail: {},
    };
  },
  async mounted() {
    this.SET_LOADING(true);
    console.log(this.$route);
    console.log(this.$route.params.id);
    const { id } = this.$route.params;
    const { data } = await movieApi.movieDetail(id);
    // axios 요청 보내기
    console.log(data);
    this.movieDetail = data;
    this.SET_LOADING(false);
    // backdro
  },
  computed:{
    movie(){
      return this.$store.state.movie
    },
    vote(){
      return this.movie?.vote_average/2
    },
    imgSrc(){
      return `https://image.tmdb.org/t/p/original${this.movie?.poster_path}`
    },
    backdropImgSrc(){
      return `https://image.tmdb.org/t/p/original${this.movie?.backdrop_path}`
    },
    isLiked(){
      return this.$store.state.movieLike
    },
  },
  methods: {
    ...mapMutations(["SET_LOADING"]),
    beforeCreate(){
      this.$store.dispatch('getDetail', this.$route.params.id)
      },
    mounted(){
      this.$store.dispatch('getDetail', this.$route.params.id)
    },
      getLike(){
        this.$store.dispatch('getLike', this.$route.params.id)
      },
    image(img) {
      console.log();
      return `https://image.tmdb.org/t/p/original/${img}`;
    },
    youtube(src) {
      return `https://www.youtube.com/embed/${src}`;
    },
  },
};
</script>

<style>
.movie-detail {
  /* z-index: 99; */
  position: relative;
  padding: 40px 40px;
  margin-top: 100px;
}
.movie-detail-image {
  background-size: cover;
  height: 100vh;
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  z-index: 0;
  margin-top: 100px;
  /* filter: grayscale(px); */
}
.movie-detail-image::after {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  min-height: 100vh;
  background-color: rgb(40, 40, 40);
  opacity: 0.8;
  content: "";
  display: block;
  margin-top: 100px;
  
}
.movie-content {
  position: relative;
  z-index: 999;
}
.movie-title {
  margin-left: 5px;
}
.movie-information-wrapper {
  font-size: 13px;
}
.genres {
  display: flex;
  align-items: center;
}
.genres:not(:first-of-type)::before {
  content: "/";
  /* background-color: white; */
  /* display: inline-block; */
  margin-bottom: 4px;
  margin-left: 6px;
  margin-right: 1px;
  font-size: 20px;
}
.movie-overview {
  max-width: 60%;
  font-size: 14px;
  color: #dddddddd;
}
.homepage-link:hover {
  opacity: 0.5;
}
/* .aa {
  min-height: 100vh;
  background-color: rgb(40, 40, 40);
  opacity: 0.8;
} */
</style>