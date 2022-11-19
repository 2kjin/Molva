<template>
  <div style="padding: 0 auto;">
<!-- BACKDROP IMAGE AND MOVIE OVERVIEW -->
    <section id="backdrop" 
    :style="{'background-image':' linear-gradient(rgba(0, 0, 0,0.5), rgba(0, 0, 0,0.5)),url('+ backdropImgSrc +')'}"
    style="background-size:cover">
      <div id="backdrop-content">
        <p style="min-width: 500px; font-size: 60px;">{{movie.title}}</p>
        <div class="overview">{{movie.overview}}</div>
      </div>
    </section>

<!-- MOVIE POSTER AND DETAIL -->
    <section id="movie-detail">
      <img :src="imgSrc" class="poster">
      <div class="movie-detail-content" style="min-width: 500px; margin-left: 600px;">
        
<!-- RATINGS -->
        <v-rating
            style="display:inline-block; margin-bottom: 5px;"
            class="rating"
            background-color="amber"
            :value="movie.vote_average/2"
            color="amber"
            dense
            half-increments
            readonly
            size="22"
          ></v-rating>

<!-- GENRES -->
        <div><span class="detail-title">Genres | </span> 
          <span style="margin: 0 7px;"
          v-for="(genre, idx) in movie.genres" :key="idx">{{genre.name}}</span>
        </div>

        <div><span class="detail-title">Release Date | </span>{{movie.release_date}}</div>

<!-- ACTORS -->
        <div><span class="detail-title">Actors  | </span > 
          <span style="margin: 0 7px;"
          v-for="(actor, idx) in movie.actors" :key="idx">{{actor.name}}</span>
        </div>
        <!-- <h5>like icon</h5> -->

        <div><span class="detail-title">Vote Count | </span>{{movie.vote_count}}</div>
      </div>
    </section>
    
<!-- MOVIE REVIEW LIST AND REVIEW FORM -->
    <section style="margin: 70px 350px; min-width: 700px; max-width: 1200px;">
      <span style="font-size: 30px; margin: 0 20px;">Reviews</span>
      <span class="form-btn" @click="formClicked">Write Review</span>
      <hr>

<!-- REVIEW FORM -->
      <detail-review-form v-if="isFormViewed" :movie="movie"/>

<!-- REVIEW LIST -->
      <div id="reivew-list">
      </div>
    </section>
  </div>

</template>

<script>
import DetailReviewForm from '@/components/DetailReviewForm'
export default {
  name:'DetailView',
  components:{
    DetailReviewForm
  },
  data(){
    return {
      isFormViewed:false,
    }
  },
  computed:{
    movie(){
      return this.$store.state.movie
    },
    imgSrc(){
      return `https://image.tmdb.org/t/p/original${this.movie.poster_path}`
    },
    backdropImgSrc(){
      return `https://image.tmdb.org/t/p/original${this.movie.backdrop_path}`
    },
  },
  methods:{
    // form button 클릭시 form 열고 닫기 (innertext 변경)
    formClicked(){
      const btnText = document.querySelector('.form-btn')
      if (this.isFormViewed){
        this.isFormViewed = false;
        btnText.innerText = 'Write Review'
      } else {
        this.isFormViewed = true;
        btnText.innerText = 'Hide Form'
      }
    },
  },
  beforeCreate(){
    this.$store.dispatch('getDetail', this.$route.params.id)
  },
  // 새로고침했을 때 데이터를 불러올 수 있는 방법은 ~  ?
  // mounted(){
  //   this.$store.dispatch('getDetail', this.$route.params.id)
  // }
}
</script>

<style scoped>
/* section 1 */
#backdrop{
  padding-left: 300px;
  min-width: 780px;
  height: 550px;
  margin-top: 40px;
  overflow:hidden;
}
#backdrop-content{
  margin-top: 100px;
  display:flex;
  flex-direction: column;
  justify-content: center;
  flex-wrap: wrap;
  position: relative;
}
.overview{
  min-width: 500px;
  width: 600px;
  font-size: 15px;
}
.poster{
  width: 230px;
  border-radius: 10px;
  position: absolute;
  box-shadow: 3px 3px 3px 3px rgba(0, 0, 0, 0.634);
  left: 300px;
  top: 620px;
}
.movie-detail-content div {
  margin: 30px 0;
}
.movie-detail-content div .detail-title{
  font-size: 18px;
  font-weight: bold;
}
</style>