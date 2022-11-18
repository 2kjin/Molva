<template>
  <div>
    <h1>Community Page</h1>
    <router-link :to="{ name: 'CreatePage' }">[CREATE]</router-link>
    <hr>
    <CommunityList/>
  </div>
</template>

<script>
import CommunityList from '@/components/CommunityList'


export default {
  name: 'CommunityPage',
  components: {
    CommunityList,
  },
  computed:{
    isLogin() {
      return this.$store.getters.isLogin
    }
  },
  created() {
    this.getCommunities()
  },
  methods: {
    getCommunities() {
      if (this.isLogin === true) { 
        this.$store.dispatch('getCommunities')
      } else {
        alert('로그인이 필요한 서비스 입니다.')
        this.$router.push({ name: 'LogInPage'})
      }
    }
  }
}
</script>

<style>

</style>
