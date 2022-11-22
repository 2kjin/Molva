<template>
  <form @submit.prevent="login">
    <label for="username">Username </label>
    <input type="text" id="username" v-model="username" class="userInput">  <br>

    <label for="password">Password </label>
    <input type="password" id="password" v-model="password" class="userInput"> <br>

    <input type="submit" value="Login" class="login-btn">
  </form>
</template>

<script>
export default {
  name:'LoginView',
  data(){
    return {
      username:null,
      password:null,
    }
  },
  methods:{
    login(){
      const username = this.username;
      const password = this.password;
      const payload = {
        username,
        password,
      }
      this.$store.dispatch('login', payload)

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
        window.location.reload()
      } else {
        alert('login failed !')
      }
    }
  }
}
</script>

<style scoped>
</style>