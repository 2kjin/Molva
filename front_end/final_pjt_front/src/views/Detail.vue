<template>
<div style="padding: 0 auto;">
  <div class="movie-detail" v-if="movie && movie.backdrop_path">
    <div class="container">
      <div
        class="movie-detail-image"
        :style="{ backgroundImage: ' linear-gradient(rgba(0, 0, 0,0.5), rgba(0, 0, 0,0.5)),url('+ backdropImgSrc +')'}"
      ></div>
      <div class="movie-content d-flex">
        <div style="">
          <img
            class="mt-2"
            style="height:60vh; border-radius: 10px; box-shadow: 0 10px 15px 0 #000000;"
            :src="imgSrc"
          />
        </div>

        <font-awesome-icon icon="fa-solid fa-heart" 
        v-if="isLiked==true" class="heart-btn fa-2x" @click="getLike"/>
        <font-awesome-icon icon="fa-regular fa-heart" 
        v-if="isLiked==false" class='heart-btn fa-2x' @click="getLike"/>

        <div class="ml-4 w-75">
          <h2 class="movie-title">{{ movie.title }}</h2>

          <div
              v-for="ott_path in movie.ott_paths"
              :key="ott_path.id"
            >
              <img :src='image(ott_path.ott_path)' alt="" width="50" height="50">
            </div>

          <div class="movie-information-wrapper mt-4 d-flex align-items-center">
            <div>{{ movie.release_date.split("-")[0] }}</div>

            <span class="ml-1">ㆍ</span>

            <div>{{ movie.runtime }} 분</div>

            <span class="ml-1">ㆍ</span>

            <div class="ml-2 d-flex">
              <div
                class="genres"
                v-for="genre in movie.genres"
                :key="genre.id"
              >
                {{ genre.name }}
              </div>

              <span class="ml-1 d-flex align-items-center">ㆍ</span>

              <div class="ml-2 d-flex align-items-center">
                <div> {{ movie.directors[0].name }}</div>
              </div>

              <span class="ml-1 d-flex align-items-center">ㆍ</span>

              <v-rating
              style="display:inline-block; margin-bottom: 5px;"
              class="rating d-flex align-items-center"
              background-color="amber"
              :value="movie.vote_average/2"
              color="amber"
              dense
              half-increments
              readonly
              size="22"
              ></v-rating>

            </div>

          </div>

          <div class="movie-overview mt-3">{{ movie.overview }}</div>

          <div class="movie-information-wrapper mt-4 d-flex justify-content-around">
            <div
              v-for="actor in movie.actors"
              :key="actor.id"
            >
              <img :src='image(actor.profile_path)' alt="" style=" height:10vh;">
            </div>
          </div>
          <br>
          <section>
            <span style="font-size: 30px;">Reviews</span>
            <span style="margin: 0 20px 0 10px;">( {{reviews.length}} )</span>
            <span v-if="reviewBtn" class="form-btn" @click="formClicked" >Write Review</span>
            <hr>

            <DetailReviewForm v-if="isFormViewed" :movie="movie" @close-form="isFormViewed=false" @close-btn="reviewBtn=false"
            style="margin-bottom: 20px;"/>

            <DetailReviewList :reviews="reviews"/>
          </section>
          <br><br>
          <div class="movie-youtube-area">
            관련 영상
            <hr>
            <YoutubeList :title="movie.title"/>
          </div>


        </div>
      </div>
    </div>
  </div>
</div>
</template>

<script>
import { mapMutations } from "vuex";
import YoutubeList from '@/components/YoutubeList'
import DetailReviewForm from '../components/DetailReviewForm.vue'
import DetailReviewList from '../components/DetailReviewList.vue'

export default {
  name:'DetailView',
  components:{
    YoutubeList,
    DetailReviewForm,
    DetailReviewList,
  },
  data() {
    return {
      isFormViewed:false,
      movieDetail: {},
      genres: [],
      ott: [],
    };
  },
  computed:{
    movie(){
      return this.$store.state.movie
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
    reviews(){
      return this.$store.state.reviews
    },
    reviewBtn(){
      const username = localStorage.getItem('username');      
      let res = true
      this.reviews.forEach((review)=>{
      if (review.username === username){
        res = false
        return
        }
      })
      return res
    }
  },
  methods: {
    ...mapMutations(["SET_LOADING"]),
    formClicked(){
      console.log(this.movie)
      const btnText = document.querySelector('.form-btn')
      if (this.isFormViewed){
        this.isFormViewed = false;
        btnText.innerText = 'Write Review'
      } else {
        this.isFormViewed = true;
        btnText.innerText = 'Hide Form'
      }
    },
    getLike(){
      this.$store.dispatch('getLike', this.$route.params.id)
      },
    image(img) {
      return `https://image.tmdb.org/t/p/original/${img}`;
    },
  },
  created() {
    this.$store.dispatch('getDetail', this.$route.params.id),
    this.$store.dispatch('getReviews', this.$route.params.id)
  },
};
</script>

<style>
.movie-detail {
  position: relative;
  margin: auto;
  margin-top: 70px;
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
  margin-top: 90px;
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
  margin-top: 90px;
  
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