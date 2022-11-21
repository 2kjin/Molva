<template>
  <div>
    <b-form @submit.prevent="onSearch">
        <b-form-input class="border-black" v-model="keyword" placeholder="영화 제목을 입력하세요."></b-form-input>
    </b-form>
    <SearchMovieText v-if="movieList" :text="'Search Result'"></SearchMovieText>
    <SearchMovieLists :movieList="movieList"></SearchMovieLists>
  </div>
</template>

<script>
import SearchMovieLists from "../components/SearchMovieLists";
import SearchMovieText from "../components/SearchMovieText";
import { movieApi } from '../utils/axios';
import { mapMutations } from "vuex";
export default {
    data(){
        return {
            keyword:"",
            movieList:""
        }
    },
components:{
    SearchMovieText,
    SearchMovieLists
},
created(){
  this.SET_LOADING(false);
},
methods:{
    ...mapMutations(["SET_LOADING"]),
    async onSearch(){
        this.SET_LOADING(true);
        console.log(this.keyword);
        if(!this.keyword){
            alert("영화 제목을 입력하세요!");
            this.keyword = ""
            return;
        }
        const {data} = await movieApi.search(this.keyword);
        console.log(data);
        this.movieList=data.results;
        this.SET_LOADING(false);
        this.keyword = ""
    }    
}

}
</script>

<style>
.search-input{
    color:black;
}
</style>