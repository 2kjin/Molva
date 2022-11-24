<template>
  <div class="d-flex flex-wrap" v-if="movieList">
    <div
      class="movie-card"
      style="width:125px;"
      v-for="li in movieList"
      :key="li.id"
    >
    <!-- <p>{{movieList}}</p> -->
      <div  @click="goDetail(li.movie_id)" v-if="li">
        <b-img style="width:125px; height:180px; border-radius: 7px; box-shadow: 0 7px 10px 0 #000000;" v-if="li.poster_path" fluid :src="image(li.poster_path)" alt="Image 2"></b-img>
        <b-img style="width:125px; height:180px; border-radius: 7px; box-shadow: 0 7px 10px 0 #000000;" v-else fluid :src="noImage" alt="Image 2"></b-img>
        <div class="movie-information">
          <div class="movie-title">{{ li.title }}</div>
            <div>
              <v-rating
              class="rating"
              background-color="amber"
              :value="li.vote_average / 2"
              color="amber"
              dense
              half-increments
              readonly
              size="18"
              style="margin: 3px 0"
              ></v-rating>
          </div>
          <div class="movie-date" v-if="li.release_date">{{ li.release_date.split("-")[0] }}</div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  // props: ['movieList'],
  props: {
    movieList: Array,
  },
  data(){
    return {
      noImage: require("../assets/error.png")
    }
  }
,
  methods: {
    image(img) {
      return `https://image.tmdb.org/t/p/w300/${img}`;
    },
     goDetail(id){
      this.$router.push(`${id}`);
      console.log(id)
    }
  },
};
</script>

<style></style>