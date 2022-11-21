<template>
  <div id="myprofile">
    <!-- SIDEBAR -->
    <div id="sidebar">
      <span>Hello, <span style="font-size: 24px ">Username</span></span>
      <div class="profile" style="background-color:#c3ddecd0; width: 100%;">
        <div><span>123</span><span>123</span><span>123</span></div>
        <div style="font-size:10px"><span>Reviews</span><span>Followers</span><span>Following</span></div>
      </div>
      <div class="bar-item" @click="isClicked('favorites')" :class="{'is-selected': this.favorites}">Favorites</div>
      <div class="bar-item" @click="isClicked('reviews')" :class="{'is-selected': this.reviews}">My Review</div>
      <div class="bar-item" @click="isClicked('history')" :class="{'is-selected': this.history}">Movie History</div>
    </div>

    <!-- CONTENT -->
    <div id="content" style="padding: 50px 90px;">
      <my-review v-if="this.reviews"/>
      <my-favorites v-if="this.favorites"/>
      <my-history v-if="this.history"/>
    </div>
  </div>
</template>

<script>
import MyReview from '@/components/MyReview'
import MyFavorites from '@/components/MyFavorites'
import MyHistory from '@/components/MyHistory'
export default {
  name:'MyProfileView',
  components:{
    MyReview,
    MyFavorites,
    MyHistory,
  },
  data(){
    return{
      favorites:true,
      reviews:false,
      history: false,
    }
  },
  methods:{
    isClicked(params){
      if (params==='reviews'){
        this.reviews=false
        this.favorites=false
        this.history=false
      } else if (params==='favorites'){
        this.reviews=false
        this.favorites=true
        this.history=false
      } else {
        this.reviews=false
        this.favorites=false
        this.history=true
      }
    }
  }
}
</script>

<style scoped>
#myprofile {
  display:flex;
  justify-content: center;
  margin-top: 7vh;
}
#sidebar,
#content {
  border: 3px solid #e0d598;
  border-radius: 10px;
  height: 80vh;
  margin: 0 20px;
}
#sidebar{
  font-size: 20px;
  padding-bottom: 30px;
  min-width: 200px;
  width: 15%;
  text-align: center;
  display: flex;
  flex-direction: column;
  justify-content: space-evenly;
}
.profile {
  color: #23262b;
  height: 80px;
  padding-top: 20px;
}
#content{
  min-width: 500px;
  width: 55%;
}
.bar-item{
  transition: transform 0.2s linear;
}
.bar-item:hover{
  cursor:pointer;
  transform: scale(1.05);
}
.bar-item:active{
  transform: translateY(10px);
}
.is-selected{
  font-size: 22px;
  font-weight: bold;
  color:#e0d598;
}
</style>