<template>

  <form @submit.prevent="signUp">
    <label for="username">Name </label>
    <input type="text" id="username" v-model="username" class="userInput">  <br>

    <label for="password1">Password </label>
    <input type="password" id="password1" v-model="password1" class="userInput"> <br>
    
    <label for="password2">Password confirmation </label>  
    <input type="password" id="password2" v-model="password2" class="userInput">  <br>

    <input type="submit" value="Signup" class="signup-btn" >
  </form>

</template>

<script>
export default {
  name:'SignupView',
  data(){
    return {
      username:null,
      password1:null,
      password2:null,
    }
  },
  methods:{
    signUp(){
      const username = this.username
      const password1 = this.password1
      const password2 = this.password2

      const payload ={
        username,
        password1,
        password2
      }
      this.$store.dispatch('signUp', payload)
      this.username = null
      this.password1 = null
      this.password2 = null
    },
  },
  computed: {
    isLogin () {
      return this.$store.getters.isLogin
    }
  },
  watch:{
    isLogin(){
      if (this.isLogin){
        this.$emit('send-close-sign')
        this.$store.dispatch('getUser', this.username)
      } else {
        alert('login failed !')
      }
    }
  }
}
</script>

<style>
label{
  font-size: 20px;
  margin-top: 20px;
}
#username,
#password1,
#password2,
#password{
  padding: 10px;
  width: 100%;
  border-bottom: 1px solid #e4d790;
}
.signup-btn,
.login-btn{
  margin-top: 50px;
  margin-left: 270px;
  text-align: center;
  font-weight: bold;
  font-size: 18px;
  color: #353A40;
  width: 80px;
  height: 40px;
  background-color: #e4d790;
  border-radius: 10px;
  transition: transform 0.1s;
}
.login-btn{
  margin-top: 150px;
}
.signup-btn:hover,
.login-btn:hover{
  cursor: pointer;
  transform: scale(1.05);
}
.signup-btn:active,
.login-btn:active {
  background-color: #e4d790;
  box-shadow: 0 5px rgb(97, 97, 97)83a;
  transform: translateY(4px);
}
/* input[type=text]:focus{
  outline: none;
  caret-color: #F8F9FA;
  color: #F8F9FA;
}
.userInput:focus{
  outline: none;
  caret-color: #F8F9FA;
  color: #F8F9FA;
} */
</style>