<template>
  <div>
    <b-form @submit.prevent="onSearch">
        <b-form-input class="border-black" v-model="keyword" placeholder="영화 제목을 입력하세요."></b-form-input>
    </b-form>
    <MovieText v-if="movieList" :text="'Search Result'"></MovieText>
    <MovieLists :movieList="movieList"></MovieLists>
  </div>
</template>

<script>
import MovieLists from "@/components/MovieLists";
import MovieText from "@/components/MovieText";
import { movieApi } from '../utils/axios';
import { mapMutations } from "vuex";
export default {
    name: 'SearchView',
    data(){
        return {
            keyword:"",
            movieList:""
        }
    },
components:{
    MovieText,
    MovieLists
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