<template>
  <div id="modal-content" >
    <div class="modal-content-half" ></div>
    <div id="forms">
      <div id="buttons">
        <span :class="{is_selected:loginViewed}"
        @click="isClicked('login')">Login</span>
        <span :class="{is_selected:signupViewed}"
        @click="isClicked('signup')">Signup</span>
      </div>
      <login-view v-if="loginViewed"/>
      <signup-view v-if="signupViewed"/>
    </div>
  </div>

</template>

<script>
import LoginView from '@/components/LoginView.vue'
import SignupView from '@/components/SignUpView.vue'
export default {
  name:'ModalViewContent',
  data(){
    return{
      loginViewed : true,
      signupViewed : false,
    }
  },
  components: { 
    LoginView,
    SignupView,
  },
  methods:{
    isClicked(params){
      if (params==='login'){
        this.loginViewed = true
        this.signupViewed = false
      } else {
        this.signupViewed = true
        this.loginViewed = false
      }
    }
  }
}
</script>

<style scoped>
#modal-content{
  display: flex;
}
a{
  text-decoration: none;
}
.modal-content-half{
  margin: 0;
  width: 50%;
  min-height: 500px;
  background-color:#C3DDEC;
  border-radius: 10px 0 0 10px;;
}
#buttons{
  padding-left: 150px;
}
#buttons span{
  padding-bottom: 10px;
  margin: 0 10px;
  margin-bottom: 25px;
  font-size: 20px;
  text-align: center;
  display: inline-block;
  width: 80px;
  transition: transform 0.3s linear;
}
#buttons span:hover{
  cursor:pointer;
  transform: scale(1.2)
}
.is_selected{
  border-bottom: 1px solid #C3DDEC;
}
#forms{
  max-width: 50%;
  padding: 20px;
  padding-bottom: 35px;
}
</style>