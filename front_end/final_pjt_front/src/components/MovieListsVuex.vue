<template>
 <div class="d-flex flex-wrap" v-if="nowPlaying">
    <div
      class="movie-card"
      style="width:125px;"
      v-for="li in nowPlaying"
      :key="li.id"
    >
      <div @click="goDetail(li.id)" v-if="li" >
        <b-img fluid :src="image(li.poster_path)" alt="Image 2"></b-img>
        <div class="movie-information">
          <div class="movie-title">{{ li.title }}</div>
          <div class="movie-date">{{ li.release_date.split("-")[0] }}</div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>

import { mapState } from 'vuex';
export default {


  computed:{
    ...mapState(["nowPlaying"])
  },
  methods: {
    image(img) {
      return `https://image.tmdb.org/t/p/w300/${img}`;
    },
    goDetail(id){
      // console.log(id);
      this.$router.push(`detail/${id}`);
    }
  },
};

</script>
<style></style>
