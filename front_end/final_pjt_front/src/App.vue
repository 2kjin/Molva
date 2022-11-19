<template>
  <v-app>
    <div id="appbar">
      <router-link :to="{ name:'home' }"><img src="@/assets/f_molva.png" alt="logo" id="logo"/></router-link>
      <v-tabs>
        <v-tab><router-link :to="{name:'home'}" style="text-decoration: none; color:#C3DDEC ">HOME</router-link></v-tab>
        <v-tab style="color:#C3DDEC">COMMUNITY</v-tab>
        <v-tab><router-link :to="{name:'blog'}" style="text-decoration: none; color:#C3DDEC">MY BLOG</router-link></v-tab>
        <router-link to="/search">Search</router-link>
        <b-spinner
          class="d-block ml-auto mr-auto"
          v-if="loading"
          label="Spinning"
        ></b-spinner>
        <!-- 토큰 여부에 따라 login / logout 버튼 교체 -->
        <div id="logout" v-if="this.$store.state.token">LOGOUT</div>
        <div id="login" v-else-if="!this.$store.state.token"
        @click="isModalViewed=true"
        >LOGIN/SIGNUP</div>
      </v-tabs>
    </div>

    <modal-view
    id="modalView"
    v-if="isModalViewed"
    @close-modal="isModalViewed=false">
      <modal-view-content/>
    </modal-view>
    <router-view/>
    <footer>
      © 2022. Molva Co. all rights reserved.
    </footer>
  </v-app>
</template>

<script>
import { mapState } from "vuex"
import ModalViewContent from '@/components/ModalViewContent.vue'
import ModalView from '@/components/ModalView.vue'
export default {
  name: 'App',
  data(){
    return {
      isModalViewed: false,
    }
  },
  components: {
    ModalViewContent,
    ModalView
    ...mapState(["loading"]),
  },  
};
</script>

<style>
@import url("https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@100;300;400&display=swap");
* {
  font-family: Cambria, Cochin, Georgia, Times, 'Times New Roman', serif;
}
#app{
  background-color: #23262b;
  color: #F8F9FA;
  position: relative;
}
#modalView{
  position: absolute;
}
div.v-tabs{
  margin: 20px 40px 0 0;
}
div.v-slide-group__wrapper{
  background-color: #23262b;
  color:#C3DDEC;
}
div.v-tab{
  margin-left: 5px;
}
div.v-slide-group__content{
  margin: 0 auto;
  display: flex;
  justify-content: flex-end;
  align-items: center;
}
#logout,
#login {
  margin: 10px;
  padding: 9.5px 0;
  text-align: center;
  font-weight: bold;
  font-size: 13px;
  color: #353A40;
  width: 100px;
  height: 40px;
  background-color: #C3DDEC;
  border-radius: 10px;
  margin-right: 20px;
  box-shadow: 0 0 3px 3px #35383a;
  transition: transform 0.1s;
}
#logout:hover,
#login:hover{
  cursor: pointer;
  transform: scale(1.05);
}
#logout:active,
#login:active {
  background-color: #C3DDEC;
  box-shadow: 0 5px rgb(97, 97, 97)83a;
  transform: translateY(4px);
}
#appbar{
  display:flex;
  align-items: center;
}
#logo{
  margin: 20px 0 0 40px;
  width: 170px;
}
footer{
  margin-top: 30px;
  color:#5e6572;
  width: 100%;
  height: 10vh;
  display:flex;
  justify-content: center;
  align-items: center;
}
</style>