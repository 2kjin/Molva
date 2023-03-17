<template>
  <v-app>
    <div id="appbar">
      <router-link :to="{ name:'home' }"><img src="@/assets/f_molva.png" alt="logo" id="logo"/></router-link>
      <v-tabs>
        <span>
          <v-tab><router-link :to="{name:'home'}" style="text-decoration: none; color:#e0d598 ">HOME</router-link></v-tab>
        </span>
        <span v-if="isLogin">
          <v-tab><router-link :to="{name:'today'}" style="text-decoration: none; color:#e0d598 ">TODAY?</router-link></v-tab>
        </span>
        <span v-if="isLogin">
          <v-tab><router-link :to="{name:'random'}" style="text-decoration: none; color:#e0d598 ">RANDOM</router-link></v-tab>
        </span>
        <span v-if="isLogin">
          <v-tab><router-link :to="{name:'search'}" style="text-decoration: none; color:#e0d598">SEARCH</router-link></v-tab>
        </span>
        <!-- <span v-if="isLogin">
          <v-tab><router-link :to="{name:'community'}" style="text-decoration: none; color:#e0d598">COMMUNITY</v-tab>
          <v-tab><router-link :to="{name:'profile'}" style="text-decoration: none; color:#e0d598">PROFILE</router-link></v-tab>
        </span> -->
          <!-- 토큰 여부에 따라 login / logout 버튼 교체 -->
          <div id="logout" v-if="this.$store.state.token"
            @click="logOut"
          >LOGOUT</div>
          <div id="login" v-else-if="!this.$store.state.token"
          @click="isModalViewed=true"
          >LOGIN/SIGNUP</div>
      </v-tabs>
    </div>

    <modal-view
    id="modalView"
    v-if="isModalViewed"
    @close-modal="isModalViewed=false"
    >
    <modal-view-content/>
    </modal-view>
    <b-spinner
      class="d-block ml-auto mr-auto"
      v-if="loading"
      label="⭐"
    ></b-spinner>
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
      loginSwitch: false,
    }
  },
  components: {
    ModalViewContent,
    ModalView,
  },
  computed: {
    ...mapState(["loading"]),
    isLogin(){
      return this.$store.getters.isLogin
    },
  },
  methods: {
    logOut(){
      this.$store.dispatch('logOut')
    }
  },
  watch: {
    isLogin(){
      this.isModalViewed = false
    }
  }  
};
</script>

<style>
@import url('https://fonts.googleapis.com/css?family=Abril+Fatface|Lato');
* {
  font-family: 'Lato', sans-serif;
}

#app{
  background-color: #23262b;
  color: #ffffff;
  position: relative;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  min-height: 100vh;
}
#modalView{
  position: absolute;
}
div.v-tabs{
  margin: 20px 40px 0 0;
}
div.v-slide-group__wrapper{
  background-color: #23262b;
  color:#e4d790;
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
  background-color: #e4d790;
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
  background-color: #e4d790;
  box-shadow: 0 5px rgb(97, 97, 97)83a;
  transform: translateY(4px);
}
#appbar{
  display:flex;
  align-items: center;
}
#logo{
  margin: 30px 0 0 40px;
  width: 200px;
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